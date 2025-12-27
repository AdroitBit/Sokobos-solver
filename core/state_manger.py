from collections import Counter
import copy
from core.enums import HeightLayer, PushDirection
from core.object_base import InGameObject
from objects.movable import Vase
from objects.object_with_goals import InGameObjectWithGoal
from objects.player import Player
from objects.static import Wall
import cv2
import numpy as np

class State:
    """
    If we look the state as graph of node,
    We can use breadth first search, And it can avoid circular move.

    examples
    ```
        objects = []
        objects.append(Player())
        objects.append(Vase())
        ...
        w = 3
        h = 3
        state = State(w,h,objects)
    ```

    """

    def __init__(self, w, h, in_game_objects:list['InGameObject'], goal_objects:list['InGameObject']):
        self.w = w
        self.h = h
        self.in_game_objects = in_game_objects # flat list of all objects
        self.goal_objects = goal_objects
        self.log_messages = []

    def is_valid_position(self, x, y):
        return 0 <= x < self.w and 0 <= y < self.h
    
    def get_objects_at(self, x:int, y:int) -> list['InGameObject']:
        if not self.is_valid_position(x, y):
            return []
        
        r=[]
        for obj in self.in_game_objects:
            #use shape definition
            origin_x = obj.x
            origin_y = obj.y
            shape = obj.appearance_definition.pattern
            break_check_on_current_obj=False
            for dy in range(obj.appearance_definition.rough_height):
                if break_check_on_current_obj==True:
                    break
                for dx in range(obj.appearance_definition.rough_width):
                    if shape[dy][dx]: #if this part of shape is occupied
                        if origin_x + dx == x and origin_y + dy == y:
                            r.append(obj)
                            break_check_on_current_obj=True
                            break
        return r
    
    def get_object_at(self, x:int, y:int, h:HeightLayer) -> 'InGameObject|None':
        objects = self.get_objects_at(x, y)
        for obj in objects:
            if obj.height_layer == h:
                return obj
        return None

    def is_same_state(self, other_state) -> bool:
        #questionable method, might fix later
        if self.w != other_state.w or self.h != other_state.h:
            return False

        for y in range(self.h):
            for x in range(self.w):
                self_objects = self.map[y][x].objects
                other_objects = other_state.map[y][x].objects

                if len(self_objects) != len(other_objects):
                    return False

                self_counter = Counter(type(obj) for obj in self_objects)
                other_counter = Counter(type(obj) for obj in other_objects)

                if self_counter != other_counter:
                    return False

        return True
    
    

    def remove_object(self, obj:'InGameObject'):
        if obj in self.in_game_objects:
            self.in_game_objects.remove(obj)

    def clone(self) -> 'State':
        return copy.deepcopy(self)
    
    def get_player(self) -> Player|None:
        r=None
        for obj in self.in_game_objects:
            if obj.__class__==Player:
                r=obj
                break
        return r


    
    def step(self, direction:PushDirection) -> "State | None":
        """
        Apply ONE move.
        Returns:
            - new State if move is valid
            - None if move is invalid
        """
        new_state = self.clone()

        player = new_state.get_player()
        get_object_at_x = player.x
        get_object_at_y = player.y

        if direction==PushDirection.LEFT:
            get_object_at_x-=1
        elif direction==PushDirection.RIGHT:
            get_object_at_x+=1
        elif direction==PushDirection.UP:
            get_object_at_y-=1
        elif direction==PushDirection.DOWN:
            get_object_at_y+=1

        #assume only 1 height layer for now
        obj_in_that_direction = new_state.get_object_at(get_object_at_x, get_object_at_y, HeightLayer.ON_GROUND)
        if obj_in_that_direction is None:
            player.x+=direction[0]
            player.y+=direction[1]
            return new_state
        else:
            #chain of InteractionResult
            #vase against pot
            #None from interaction result is the cut of chain -> no execution, return None state

            #random pick object...cus skip some logic
            current_obj_prev = player
            current_obj = obj_in_that_direction
            interaction_results=[]
            while True:
                if current_obj is None:
                    break
                # print(current_obj)
                interaction_result = current_obj.on_pushed_by(current_obj_prev,direction)
                if interaction_result is None:
                    # print("bruh")
                    return None
                if interaction_result.move_object is not None:
                    current_obj_prev = current_obj
                    current_obj = new_state.get_object_at(
                        interaction_result.move_object[1],
                        interaction_result.move_object[2],
                        HeightLayer.ON_GROUND
                    )
                else:
                    current_obj_prev = current_obj
                    current_obj = None
                
                    
                
                interaction_results.append(interaction_result)

            if None in interaction_results:
                return None
            else:
                #apply interaction result
                for interaction_result in interaction_results:
                    if interaction_result.move_object is not None:
                        obj_to_move = interaction_result.move_object[0]
                        obj_to_move.x = interaction_result.move_object[1]
                        obj_to_move.y = interaction_result.move_object[2]

                    if interaction_result.removed_objects is not None:
                        for o in interaction_result.removed_objects:
                            new_state.remove_object(o)
                player.x=get_object_at_x
                player.y=get_object_at_y
                if new_state.is_deadlock()==True:
                    return None
                return new_state

    def __hash__(self):
        data = []
        for obj in self.in_game_objects:
            data.append((obj.__class__.__name__, obj.x, obj.y))
        return hash(tuple(sorted(data)))

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return hash(self) == hash(other)
    

    def is_completed(self) -> bool:
        "Level is solve if all goal objects are satisfied"
        fulfilled=[]
        for goal_obj in self.goal_objects:
            in_game_obj = self.get_object_at(goal_obj.x,goal_obj.y,HeightLayer.ON_GROUND)
            if in_game_obj is None:
                return False
            else:
                con1 = goal_obj.__class__ == in_game_obj.__class__
                con2 = goal_obj.appearance_definition.rotation_degree == in_game_obj.appearance_definition.rotation_degree
                fulfilled.append(con1 and con2)
        if len(fulfilled)!=len(self.goal_objects):
            return False
        else:
            return all(fulfilled)

    def is_deadlock(self) -> bool:
        in_game_objects_that_has_goal = []
        in_game_objects_goaless = []
        for in_game_obj in self.in_game_objects:
            if isinstance(in_game_obj, InGameObjectWithGoal):
                in_game_objects_that_has_goal.append(in_game_obj)
            else:
                in_game_objects_goaless.append(in_game_obj)
        
        #amount of goal object is not equal (or less than, but preferably equal) to amount of destination -> deadlock
        if len(in_game_objects_that_has_goal)!=len(self.goal_objects):
            return True
        
        #if there walls cover two direction of object with goal -> deadlock
        for in_game_obj_with_goal in in_game_objects_that_has_goal:
            direction_pairs=[
                (PushDirection.UP,PushDirection.LEFT),
                (PushDirection.UP,PushDirection.RIGHT),
                (PushDirection.DOWN,PushDirection.LEFT),
                (PushDirection.DOWN,PushDirection.RIGHT),
            ]
            for direction1,direction2 in direction_pairs:
                if isinstance(self.get_object_at(in_game_obj_with_goal.x+direction1[0],in_game_obj_with_goal.y+direction1[1], HeightLayer.ON_GROUND),Wall) and isinstance(self.get_object_at(in_game_obj_with_goal.x+direction2[0],in_game_obj_with_goal.y+direction2[1], HeightLayer.ON_GROUND),Wall):
                    #in_game_obj_with_goal already cornered here
                    touch_goal_spot = []#must be all False to deadlock
                    for goal_obj in self.goal_objects:
                        con1 = in_game_obj.x==goal_obj.x and in_game_obj.y==goal_obj.y
                        con2 = goal_obj.__class__ == in_game_obj.__class__
                        con3 = goal_obj.appearance_definition.rotation_degree == in_game_obj.appearance_definition.rotation_degree

                        is_in_its_spot = con1 and con2 and con3
                        touch_goal_spot.append(is_in_its_spot)

                    return all(x==False for x in touch_goal_spot)
        
        #


        # for y in range(0,self.h-1):
        #     for x in range(0,self.w-1):


        # return False


            

    #For A*
    def get_goal_tiles(self):
        return self.goal_objects
    def get_fragments(self):
        return [in_game_obj for in_game_obj in self.in_game_objects if isinstance(in_game_obj,InGameObjectWithGoal)]
    def get_goal_objects(self):
        pass
    def hash(self):
        objs = tuple(
            sorted(
                (obj.__class__.__name__, obj.x, obj.y)
                for obj in self.in_game_objects
                if not isinstance(obj, Player)
            )
        )
        p = self.get_player()
        return (p.x, p.y, objs)
    def is_goal(self):
        return self.is_completed()


    def render_as_image(self,name,waitKey:int=1, destroyAllWindowsAfter:bool=False):
        cell_size=25
        img = np.zeros((cell_size*self.h,cell_size*self.w,3),dtype=np.uint8)

        game_obj:InGameObject=None

        for game_obj in sorted(self.in_game_objects,key=lambda x:x.height_layer):
            n_img = cv2.imread(game_obj.appearance_definition.get_img_url_for_render())
            n_img = cv2.resize(n_img, (cell_size,cell_size))

            img[game_obj.y*cell_size:game_obj.y*cell_size+cell_size, game_obj.x*cell_size:game_obj.x*cell_size+cell_size] = n_img
            




        cv2.imshow(name,img)
        cv2.waitKey(waitKey)
        if destroyAllWindowsAfter:
            cv2.destroyAllWindows()
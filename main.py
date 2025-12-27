import heapq
from objects.hazards import *
from objects.player import Player
from objects.static import *
from objects.object_with_goals import *
from objects.movable import *

from core.state_manger import State


#original lv01
w=7+2
h=8+2
objects = []

#left and right walls
for i in range(0,h):
    wall = Wall(0,i)
    objects.append(wall)
    wall = Wall(w-1,i)
    objects.append(wall)
#top and bottom walls
for i in range(0,w):
    wall = Wall(i,0)
    objects.append(wall)
    wall = Wall(i,h-1)
    objects.append(wall)

new_objects=[
    
    Wall(1,1),
    Wall(1,4),
    Wall(1,5),
    Wall(1,6),
    Wall(1,7),
    Wall(1,8),

    LeftHeadOfStatue1(2,2,"yellow"),
    Wall(2,6),
    Wall(2,7),
    Wall(2,8),

    RightFootOfStatue1(3,5,"yellow"),
    Wall(3,7),
    Wall(3,8),

    Player(4,8),
    Wall(4,9),

    RightHeadOfStatue1(5,5,"yellow"),
    Wall(5,7),
    Wall(5,8),

    LeftFootOfStatue1(6,2,"yellow"),
    Wall(6,6),
    Wall(6,7),
    Wall(6,8),

    Wall(7,3),
    Wall(7,4),
    Wall(7,5),
    Wall(7,6),
    Wall(7,7),
    Wall(7,8),
]
objects=objects+new_objects

goal_objects=[
    LeftHeadOfStatue1(4,2,"yellow"),
    RightHeadOfStatue1(5,2,"yellow"),
    LeftFootOfStatue1(4,3,"yellow"),
    RightFootOfStatue1(5,3,"yellow")
]


# #aphrodite trial lvl01
# w=10+2
# h=7+2

# objects = []

# #left and right walls
# for i in range(0,h):
#     wall = Wall(0,i)
#     objects.append(wall)
#     wall = Wall(w-1,i)
#     objects.append(wall)
# #top and bottom walls
# for i in range(0,w):
#     wall = Wall(i,0)
#     objects.append(wall)
#     wall = Wall(i,h-1)
#     objects.append(wall)

# #other walls
# new_objects=[
#     #from (1,1) to (10,7)
#     Wall(1,1),
#     Wall(2,1),
#     Wall(3,1),
#     Wall(4,1),
#     Wall(5,1),
#     Wall(9,1),
#     Wall(10,1),

#     Wall(4,2),
#     Wall(5,2),
#     Wall(10,2),

#     Wall(2,3),
    
#     Wall(1,5),
#     Wall(2,5),
#     Wall(3,5),
#     Wall(4,5),
#     Wall(5,5),
#     Wall(9,5),
#     Wall(10,5),

#     Wall(1,6),
#     Wall(2,6),
#     Wall(3,6),
#     Wall(4,6),
#     Wall(5,6),
#     Wall(6,6),
#     Wall(8,6),
#     Wall(9,6),
#     Wall(10,6),

#     Wall(1,7),
#     Wall(2,7),
#     Wall(3,7),
#     Wall(4,7),
#     Wall(5,7),
#     Wall(6,7),
#     Wall(8,7),
#     Wall(9,7),
#     Wall(10,7),
# ]
# objects=objects+new_objects




# objects.append(MiddleOfBenchObject(3,3,color="yellow"))
# objects.append(Vase(4,3))
# objects.append(Pot(4,4))
# objects.append(Vase(6,4))
# objects.append(Pot(6,5))
# objects.append(Vase(7,4))
# objects.append(Pot(7,5))
# objects.append(Pot(8,4))
# objects.append(Pot(8,5))
# objects.append(LeftOfBenchObject(8,3,color="yellow"))
# objects.append(RightOfBenchObject(9,4,color="yellow"))
# objects.append(Vase(7,6))
# objects.append(Player(7,7))


# goal_objects = [
#     LeftOfBenchObject(6,1,color="yellow"),
#     MiddleOfBenchObject(7,1,color="yellow"),
#     RightOfBenchObject(8,1,color="yellow")
# ]

# #test wall object vase chain
# w=5+2
# h=1+2

# objects=[]
# #left and right walls
# for i in range(0,h):
#     wall = Wall(0,i)
#     objects.append(wall)
#     wall = Wall(w-1,i)
#     objects.append(wall)
# #top and bottom walls
# for i in range(0,w):
#     wall = Wall(i,0)
#     objects.append(wall)
#     wall = Wall(i,h-1)
#     objects.append(wall)

# new_objects=[
#     Wall(1,1),
#     MiddleOfBenchObject(2,1,"yellow"),
#     Vase(3,1),
#     Player(4,1)
# ]
# objects=objects+new_objects

# goal_objects=[]


state = State(
    w,
    h,
    objects,
    goal_objects
)



from collections import deque
from core.enums import PushDirection
import os

def bfs_solve(initial_state: State):
    queue = deque()
    visited = set()

    queue.append((initial_state, []))
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()
        # os.system("cls")
        print(" ".join(PushDirection._names[d] for d in path))

        if state.is_completed():
            return path

        for d in [
            PushDirection.UP,
            PushDirection.DOWN,
            PushDirection.LEFT,
            PushDirection.RIGHT,
        ]:
            next_state = state.step(d)
            if next_state is None:
                continue

            if next_state in visited:
                continue

            visited.add(next_state)
            queue.append((next_state, path + [d]))

    return None


class SearchNode:
    __slots__ = ("state", "g", "h", "f", "parent", "action")

    def __init__(self, state, g, h, parent=None, action=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
        self.action = action

    def __lt__(self, other):
        return self.f < other.f

def heuristic(state):
    fragments = state.get_fragments()
    goals = state.get_goal_tiles()

    h = 0
    for frag in fragments:
        h += min(
            abs(frag.x - g.x) + abs(frag.y - g.y)
            for g in goals
        )
    return h
    
def astar(initial_state: State):
    open_set = []

    start = SearchNode(
        state=initial_state,
        g=0,
        h=heuristic(initial_state),
        parent=None,
        action=None
    )

    heapq.heappush(open_set, start)

    visited = dict()  # state_hash -> best_cost

    while open_set:
        node = heapq.heappop(open_set)
        state = node.state

        print(" ".join(PushDirection._names[d] for d in reconstruct_path(node)))

        if state.is_goal():
            return reconstruct_path(node)

        state_key = state.hash()
        if state_key in visited and visited[state_key] <= node.g:
            continue
        visited[state_key] = node.g

        for action in [
            PushDirection.UP,
            PushDirection.DOWN,
            PushDirection.LEFT,
            PushDirection.RIGHT,
        ]:
            new_state = state.step(action)
            if new_state is None:
                continue

            child = SearchNode(
                state=new_state,
                g=node.g + 1,
                h=heuristic(new_state),
                parent=node,
                action=action
            )

            heapq.heappush(open_set, child)

    return None

def reconstruct_path(node):
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    return path[::-1]



state.render_as_image("Before",waitKey=0)
# new_state=state.clone()
# new_state=new_state.step(PushDirection.RIGHT)
# new_state.render_as_image("After1",waitKey=0,destroyAllWindowsAfter=False)
# new_state=new_state.step(PushDirection.RIGHT)
# new_state.render_as_image("After2",waitKey=0,destroyAllWindowsAfter=True)

# solution = bfs_solve(state)

# if solution is None:
#     print("No solution found")
# else:
#     print("Solution:", solution)
#     print(" ".join(PushDirection._names[d] for d in solution))

solution = astar(state)
if solution is None:
    print("No solution found")
else:
    print("Solution:", solution)

new_state=state.clone()
for action in solution:
    new_state=new_state.step(action)
new_state.render_as_image("After",waitKey=0, destroyAllWindowsAfter=True)






#Testing walk in same spot

# print(state.get_player().x,state.get_player().y)

# new_state=state.step(PushDirection.LEFT)

# print(new_state.get_player().x, new_state.get_player().y)
# print(state==new_state)

# new_state=new_state.step(PushDirection.RIGHT)

# print(new_state.get_player().x, new_state.get_player().y)
# print(state==new_state)


#Going up test

# print()
# print(state.get_object_at(7,3,HeightLayer.ON_GROUND))
# print(state.get_object_at(7,4,HeightLayer.ON_GROUND))
# print(state.get_object_at(7,5,HeightLayer.ON_GROUND))
# print(state.get_object_at(7,6,HeightLayer.ON_GROUND))
# print(state.get_object_at(7,7,HeightLayer.ON_GROUND))
# print(state.get_player().x,state.get_player().y)
# print()


# print()
# new_state = state.step(PushDirection.UP)
# print(new_state.get_object_at(7,3,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,4,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,5,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,6,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,7,HeightLayer.ON_GROUND))
# print(new_state.get_player().x,new_state.get_player().y)
# print()

# print()
# new_state = new_state.step(PushDirection.UP)
# print(new_state.get_object_at(7,3,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,4,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,5,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,6,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,7,HeightLayer.ON_GROUND))
# print(new_state.get_player().x,new_state.get_player().y)
# print()

# print()
# new_state = new_state.step(PushDirection.UP)
# print(new_state.get_object_at(7,3,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,4,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,5,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,6,HeightLayer.ON_GROUND))
# print(new_state.get_object_at(7,7,HeightLayer.ON_GROUND))
# print(new_state.get_player().x,new_state.get_player().y)
# print()
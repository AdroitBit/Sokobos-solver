from core.appearance import AppearanceDefinition
from core.enums import HeightLayer, Movability, PushDirection, Rotatability
from core.object_base import InGameObject, InteractionResult


class InGameObjectWithGoal(InGameObject):
    def __init__(self,
                 appearance_definition: AppearanceDefinition,
                 height_layer: HeightLayer,
                 movability: Movability,
                 is_pusher: bool,
                 x: int,
                 y: int
                ):
        super().__init__(
            appearance_definition,
            height_layer,
            movability,
            is_pusher,
            x,
            y
        )

class TopOfPillarObject(InGameObjectWithGoal):
    """
    Movable
    """
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/pillar_top_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None

class MiddleOfPillarObject(InGameObjectWithGoal):
    """
    Movable
    """
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_QUARTER_ROTATE,
                color_to_image={
                    "yellow":"images/pillar_middle_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None

class BaseOfPillarObject(InGameObjectWithGoal):
    """
    Movable
    """
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CANNOT_ROTATE,
                color_to_image={
                    "yellow":"images/pillar_base_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None

class LeftOfBenchObject(InGameObjectWithGoal):
    """
    Docstring for LeftOfBenchObject
    """
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/bench_left_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None

class RightOfBenchObject(InGameObjectWithGoal):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/bench_right_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None

class MiddleOfBenchObject(InGameObjectWithGoal):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/bench_middle_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None
        

class LeftHeadOfStatue1(InGameObjectWithGoal):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/statue1_left_head_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None
        
class RightHeadOfStatue1(InGameObjectWithGoal):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/statue1_right_head_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None
        
class LeftFootOfStatue1(InGameObjectWithGoal):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/statue1_left_foot_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None
        
class RightFootOfStatue1(InGameObjectWithGoal):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],color,Rotatability.CAN_FULL_ROTATE,
                color_to_image={
                    "yellow":"images/statue1_right_foot_yellow.png"
                }
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                move_object=(self, self.x + direction[0], self.y + direction[1])
            )
        else:
            return None

class TileObject(InGameObjectWithGoal):
    pass

class BridgeObject(InGameObjectWithGoal):
    pass
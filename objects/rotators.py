"""
A rotator rotates any object that moves onto it 90/180 degrees.
"""
from core.appearance import AppearanceDefinition
from core.enums import HeightLayer, Movability, Rotatability
from core.object_base import InGameObject, InteractionResult


class Rotator_90_CCW(InGameObject):
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],"red",Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

    def on_pressed_by(self, other_object:'InGameObject') -> InteractionResult:
        return InteractionResult(
            rotated_object=(other_object, -90)
        )
class Rotator_90_CW(InGameObject):
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],"red",Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

    def on_pressed_by(self, other_object:'InGameObject') -> InteractionResult:
        return InteractionResult(
            rotated_object=(other_object, 90)
        )
    
class Rotator_180(InGameObject):
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],"red",Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

    def on_pressed_by(self, other_object:'InGameObject') -> InteractionResult:
        return InteractionResult(
            rotated_object=(other_object, 180)
        )
from core.appearance import AppearanceDefinition
from core.enums import HeightLayer, Movability, PushDirection, Rotatability
from core.object_base import InGameObject, InteractionResult


class Vase(InGameObject):
    """
    Regular obstacle that can be pushed around.
    """
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],"no_color",Rotatability.CANNOT_ROTATE,
                color_to_image={"no_color":"images/vase.png"}
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

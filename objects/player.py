from core.appearance import AppearanceDefinition
from core.enums import HeightLayer, Movability, Rotatability
from core.object_base import InGameObject


class Player(InGameObject):
    def __init__(self, x:int, y:int):

        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],"no_color",Rotatability.CANNOT_ROTATE,
                color_to_image={"no_color":"images/player.png"}
            ),
            HeightLayer.ON_GROUND,
            Movability.CAN_MOVE,
            is_pusher=True,
            x=x,
            y=y
        )
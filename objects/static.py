from core.appearance import AppearanceDefinition
from core.enums import HeightLayer, Movability, PushDirection, Rotatability
from core.object_base import InGameObject, InteractionResult


class Wall(InGameObject):
    """
    An unmovable wall.
    """
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],"no_color",Rotatability.CANNOT_ROTATE,
                color_to_image={"no_color":"images/wall.png"}
            ),
            HeightLayer.ON_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

    def on_pushed_by(self, other_object: 'InGameObject', direction: PushDirection) -> InteractionResult|None:
        return None


class LockedGate(InGameObject):
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],"darkgrey",Rotatability.CANNOT_ROTATE),
            HeightLayer.ON_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

    def unlock(self):
        self.height_layer = HeightLayer.IN_GROUND


class Key(InGameObject):
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],"yellow",Rotatability.CANNOT_ROTATE),
            HeightLayer.ON_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

    def on_pushed_by(self, other_object:'InGameObject', direction:PushDirection) -> InteractionResult|None:
        if other_object.is_pusher:
            return InteractionResult(
                removed_objects=[self],
                unlock_every_locked_gates=True
            )
        else:
            return None
from core.appearance import AppearanceDefinition
from core.enums import HeightLayer, Movability, Rotatability
from core.object_base import InGameObject


class TopOfPillarDestination(InGameObject):
    """
    Unmovable
    """
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],color,Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
class MiddleOfPillarDestination(InGameObject):
    """
    Unmovable
    """
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],color,Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

class BaseOfPillarDestination(InGameObject):
    """
    Unmovable
    """
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],color,Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

class LeftOfBenchDestination(InGameObject):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],color,Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

class RightOfBenchDestination(InGameObject):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],color,Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )


class MiddleOfBenchDestination(InGameObject):
    def __init__(self, x:int, y:int, color:str):
        super().__init__(
            AppearanceDefinition(1,1,[[True]],color,Rotatability.CANNOT_ROTATE),
            HeightLayer.IN_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )

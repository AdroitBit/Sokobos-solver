from core.appearance import AppearanceDefinition
from core.enums import HeightLayer, Movability, Rotatability
from core.object_base import InGameObject, InteractionResult


class Pot(InGameObject):
    """
    A pot can't be pushed, but can explode any object it touches, or pushed onto it.
    """
    def __init__(self, x:int, y:int):
        super().__init__(
            AppearanceDefinition(
                1,1,[[True]],"no_color",Rotatability.CANNOT_ROTATE,
                color_to_image={"no_color":"images/pot.png"}
            ),
            HeightLayer.ON_GROUND,
            Movability.CANNOT_MOVE,
            is_pusher=False,
            x=x,
            y=y
        )
        
    def on_pushed_by(self, other_object, direction) -> InteractionResult:
        if other_object.is_pusher==True:
            #can't be pushed directly by player
            #can't be pushed by goal object
            return None
        else:
            #can be pushed by other object, making explosion and deletion
            return InteractionResult(
                removed_objects=[self, other_object]
            )
    
class ColorPuddle(InGameObject):
    """
    A color puddle changes the color of any object that moves onto it.
    """
    pass



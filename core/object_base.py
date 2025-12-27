import copy
from core.appearance import AppearanceDefinition, Rotatability
from core.enums import HeightLayer, Movability, PushDirection
from dataclasses import dataclass


@dataclass
class InteractionResult:
    #This also applies to exeuction order
    move_object: tuple['InGameObject', int, int] | None = None
    changed_color_object: tuple['InGameObject', str] | None = None
    rotated_object: tuple['InGameObject', int] | None = None
    unlock_every_locked_gates: bool = False
    removed_objects: list['InGameObject'] = None


class InGameObject:
    def __init__(self,
                 appearance_definition:AppearanceDefinition,
                 height_layer:HeightLayer,
                 movability:Movability,
                 is_pusher:bool,
                 x:int,
                 y:int,
                 ):
        self.appearance_definition = copy.deepcopy(appearance_definition)
        self.height_layer = height_layer
        self.movability = movability
        self.is_pusher = is_pusher
        self.x = x
        self.y = y

    def on_pushed_by(self, other:'InGameObject', direction:PushDirection
                     ) -> InteractionResult | None:
        return None
    
    def on_pressed_by(self, other:'InGameObject') -> InteractionResult | None:
        return None
    
    def rotate_90_cw(self) -> bool:
        return self.appearance_definition.rotate_90_cw()
    
    def rotate_90_ccw(self) -> bool:
        return self.appearance_definition.rotate_90_ccw()
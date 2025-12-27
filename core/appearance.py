from core.enums import Rotatability

class AppearanceDefinition:
    """
    Origin of pattern is always at top-left corner.
    Docstring for AppearanceDefinition
    
    :var rough_width: Description
    :vartype rough_width: int
    :var rough_height: Description
    :vartype rough_height: int
    :var pattern: Description
    :var example: Description
    """

    """
    rough_width: int

    rough_height: int

    pattern: list[list[bool]] #2D array representing the shape where True indicates occupied cells, False indicates empty cells

    Origin of pattern is always at top-left corner.

    example:

    ShapeDefinition(3,2,[[True,True,True],[False,True,False]]) 

    ShapeDefinition(3,3,[[False,True,False],[True,True,True],[False,True,False]]) #plus shape
    """

    def __init__(self,
                 rough_width:int,
                 rough_height:int,
                 pattern:list[list[bool]],
                 color:str,
                 rotatability:Rotatability,
                 color_to_image:dict[str,str]
                 ):
        self.rough_width = rough_width
        self.rough_height = rough_height
        self.pattern = pattern
        self.color = color
        self.rotatability = rotatability
        self.rotation_degree:int = 0
        self.color_to_image = color_to_image

    def change_color(self, new_color:str):
        self.color = new_color

    def rotate_90_cw(self) -> bool:
        """
        Rotates the object 90 degrees clockwise.
        return True if rotation was successful, False otherwise.
        """
        if self.rotatability == Rotatability.CANNOT_ROTATE:
            return False
        elif self.rotatability == Rotatability.CAN_QUARTER_ROTATE:
            if self.rotation_degree == 90:
                self.rotation_degree = 0
            elif self.rotation_degree == 0:
                self.rotation_degree = 90
            return True
        elif self.rotatability == Rotatability.CAN_FULL_ROTATE:
            if self.rotation_degree == 270:
                self.rotation_degree = 0
            else:
                self.rotation_degree += 90
            return True

    
    def rotate_90_ccw(self) -> bool:
        """
        Rotates the object 90 degrees counterclockwise.
        return True if rotation was successful, False otherwise.
        """
        if self.rotatability == Rotatability.CANNOT_ROTATE:
            return False
        elif self.rotatability == Rotatability.CAN_QUARTER_ROTATE:
            #no need to change since it's only 0 and 90 degrees
            if self.rotation_degree == 90:
                self.rotation_degree = 0
            elif self.rotation_degree == 0:
                self.rotation_degree = 90
            return True
        elif self.rotatability == Rotatability.CAN_FULL_ROTATE:
            if self.rotation_degree == 0:
                self.rotation_degree = 270
            else:
                self.rotation_degree -= 90
            return True
        
    def get_img_url_for_render(self):
        return self.color_to_image[self.color]
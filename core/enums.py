class PushDirection:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    _names = {
        UP: "UP",
        DOWN: "DOWN",
        LEFT: "LEFT",
        RIGHT: "RIGHT",
    }


class Movability:
    CANNOT_MOVE = 0
    CAN_MOVE = 1

class Rotatability:
    CANNOT_ROTATE = 0
    CAN_QUARTER_ROTATE = 1
    CAN_FULL_ROTATE = 2

class HeightLayer:
    IN_DEPTH = -1 #for water, which you cannot walk over unless that tile is with COVER_GROUND
    IN_GROUND = 0 #and object's desintation
    COVER_GROUND = 1
    ON_GROUND = 2
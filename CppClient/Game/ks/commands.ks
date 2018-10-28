[EDirection]
_def = enum <byte>
    {
        Up,
        Right,
        Down,
        Left
    }


[Move]
_def = class 
id = int
direction = EDirection


[PlantBomb]
_def = class
id = int
direction = EDirection


[DefuseBomb]
_def = class
id = int
direction = EDirection

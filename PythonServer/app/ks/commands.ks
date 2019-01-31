[ECommandDirection]
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
direction = ECommandDirection


[PlantBomb]
_def = class
id = int
direction = ECommandDirection


[DefuseBomb]
_def = class
id = int
direction = ECommandDirection

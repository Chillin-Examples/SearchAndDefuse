[ECell]
_def = enum <byte>
    {
        Empty,
        SmallBombSite,
        MediumBombSite,
        LargeBombSite,
        VastBombSite,
        Wall
    }


[ESoundIntensity]
_def = enum <byte>
    {
        Weak,
        Normal,
        Strong
    }


[EAgentStatus]
_def = enum <byte>
    {
        Alive,
        Dead
    }


[Constants]
_def = class
bomb_planting_time = int
bomb_defusion_time = int
bomb_explosion_time = int
bomb_planting_score = int
bomb_defusion_score = int
bomb_explosion_score = int
score_coefficient_small_bomb_site = float
score_coefficient_medium_bomb_site = float
score_coefficient_large_bomb_site = float
score_coefficient_vast_bomb_site = float
terrorist_vision_distance = int
terrorist_death_score = int
police_death_score = int
police_vision_distance = int
sound_ranges = map<ESoundIntensity, int>
max_cycles = int


[Position]
_def = class
x = int
y = int


[Bomb]
_def = class
position = Position
explosion_remaining_time = int
planter_id = int
defuser_id = int


[Terrorist]
_def = class
id = int
position = Position
planting_remaining_time = int
footstep_sounds = list<ESoundIntensity>
status = EAgentStatus


[Police]
_def = class
id = int
position = Position
defusion_remaining_time = int
footstep_sounds = list<ESoundIntensity>
bomb_sounds = list<ESoundIntensity>
status = EAgentStatus


[World]
_def = class
width = int
height = int
board = list<list<ECell>>
scores = map<string, float>
bombs = list<Bomb>
terrorists = list<Terrorist>
polices = list<Police>
constants = Constants

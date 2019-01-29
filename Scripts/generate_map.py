# script imports
import json, sys
name = 'valleybeyond'
map_file = open('maps/{}.txt'.format(name))

map_data = map_file.readlines()
data = {'char_board': [], 'player': {'Terrorist': [], 'Police': []}}
data['constants'] = {
    'bomb_planting_time': 0,

}

row_number, col_num = 0, 0
for row in map_data:
    row = row.replace('	', '')
    row = row.replace('\n', '')

    for char in row:
        if char == 'p':
            data['player']['Police'].append({'position': [col_num, row_number], 'direction':'Up'})
        elif char == 't':
            data['player']['Terrorist'].append({'position': [col_num, row_number], 'direction':'Up'})

        col_num += 1
    col_num = 0

    row = row.replace('p', 'e')
    row = row.replace('t', 'e')

    row_number += 1
    data['char_board'].append(row)

data['constants']['bomb_planting_time'] = 7
data['constants']['bomb_defusion_time'] = 7
data['constants']['bomb_explosion_time'] = 15
data['constants']['bomb_planting_score'] = 10
data['constants']['bomb_defusion_score'] = 15
data['constants']['bomb_explosion_score'] = 20
data['constants']['score_coefficient_small_bomb_site'] = 2.5
data['constants']['score_coefficient_medium_bomb_site'] = 5
data['constants']['score_coefficient_large_bomb_site'] = 7.5
data['constants']['score_coefficient_vast_bomb_site'] = 10
data['constants']['terrorist_vision_distance'] = 5
data['constants']['police_vision_distance'] = 3
data['constants']['terrorist_death_score'] = 5
data['constants']['police_death_score'] = 10
data['constants']["strong_intensity_max_distance"] = 5
data['constants']["normal_intensity_max_distance"] = 10
data['constants']["weak_intensity_max_distance"] = 15
data['constants']['max_cycles'] = 200



with open('generated_maps/{}.json'.format(name), 'w') as outfile:
    json.dump(data, outfile)

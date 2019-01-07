# script imports
import json, sys

map_file = open('maps/{}.txt'.format(sys.argv[1]))
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
            data['player']['Terrorist'].append({'position': [row_number, col_num]})
        elif char == 't':
            data['player']['Police'].append({'position': [row_number, col_num]})

        col_num += 1
    col_num = 0

    row = row.replace('p', 'e')
    row = row.replace('t', 'e')

    row_number += 1
    data['char_board'].append(row)

data['constants']['bomb_planting_time'] = 7
data['constants']['bomb_defusion_time'] = 10
data['constants']['bomb_explosion_time'] = 15
data['constants']['bomb_planting_score'] = 2
data['constants']['bomb_defusion_score'] = 1
data['constants']['bomb_explosion_score'] = 2
data['constants']['score_coefficient_small_bomb_site'] = 2.5
data['constants']['score_coefficient_medium_bomb_site'] = 5
data['constants']['score_coefficient_large_bomb_site'] = 7.5
data['constants']['score_coefficient_vast_bomb_site'] = 10
data['constants']['terrorist_vision_distance'] = 5
data['constants']['terrorist_death_score'] = 4
data['constants']['police_vision_distance'] = 6
data['constants']['max_cycles'] = 100

with open('generated_maps/{}.json'.format(sys.argv[1]), 'w') as outfile:
    json.dump(data, outfile)

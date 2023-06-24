# This will make 4 json files, 3 are about player windows names.
#  -streams (not used)
#  -drivers
#  -all
#  #  and the 4th is the positions on the screen for each player.


import os
from json import dump

from settings import path



# Create the json folder if it doesn't exist
if not os.path.exists(f'{path}json'):
    os.makedirs(f'{path}json')



player_streams_dict = {"F1 Live — MultiViewer": "F1LIVE", "International — MultiViewer": "INT"}

player_driver_dict = {"Max Verstappen — MultiViewer": "VER", "Fernando Alonso — MultiViewer": "ALO",
                      "Sergio Perez — MultiViewer": "PER", "Lewis Hamilton — MultiViewer": "HAM",
                      "Charles Leclerc — MultiViewer": "LEC", "George Russell — MultiViewer": "RUS",
                      "Carlos Sainz — MultiViewer": "SAI", "Lance Stroll — MultiViewer": "STR",
                      "Lando Norris — MultiViewer": "NOR", "Kevin Magnussen — MultiViewer": "MAG",
                      "Esteban Ocon — MultiViewer": "OCO", "Nico Hulkenberg — MultiViewer": "HUL",
                      "Valtteri Bottas — MultiViewer": "BOT", "Alexander Albon — MultiViewer": "ALB",
                      "Yuki Tsunoda — MultiViewer": "TSU", "Guanyu Zhou — MultiViewer": "ZHO",
                      "Pierre Gasly — MultiViewer": "GAS", "Nyck De Vries — MultiViewer": "DEV",
                      "Oscar Piastri — MultiViewer": "PIA", "Logan Sargeant — MultiViewer": "SAR",
                      'Sebastian Vettel — MultiViewer': 'VET', 'Mick Schumacher — MultiViewer': 'MSC',
                      'Daniel Ricciardo — MultiViewer': 'RIC', 'Nicholas Latifi — MultiViewer': 'LAT',
                      'Liam Lawson — MultiViewer': 'LAW',
                      "Data Channel — MultiViewer": "DATA", "Driver Tracker — MultiViewer": "TRACKER"}

player_all_dict = player_driver_dict.copy()
player_all_dict.update(player_streams_dict)

with open(f'{path}\\json\\streams.json', 'w') as json_file:
    dump(player_streams_dict, json_file, indent=4)

with open(f'{path}\\json\\drivers.json', 'w') as json_file:
    dump(player_driver_dict, json_file, indent=4)

with open(f'{path}\\json\\all.json', 'w') as json_file:
    dump(player_all_dict, json_file, indent=4)

positions = [[None for _ in range(25)] for _ in range(25)]

positions[1][0] = (1, 1)
positions[1][1] = [0, 0, 1, 1]

positions[2][0] = (1, 2)
positions[2][1] = [0, 0, 1, 1]
positions[2][2] = [0, 1, 1, 1]

positions[3][0] = (2, 2)
positions[3][1] = [0, 0, 1, 1]
positions[3][2] = [1, 0, 1, 1]
positions[3][3] = [0, 1, 2, 1]

positions[4][0] = (2, 2)
positions[4][1] = [0, 0, 1, 1]
positions[4][2] = [0, 1, 1, 1]
positions[4][4] = [1, 0, 1, 1]
positions[4][3] = [1, 1, 1, 1]

positions[5][0] = (5, 6)
positions[5][1] = [0, 0, 3, 3]
positions[5][2] = [0, 3, 3, 3]
positions[5][5] = [3, 0, 2, 2]
positions[5][4] = [3, 2, 2, 2]
positions[5][3] = [3, 4, 2, 2]

positions[6][0] = (3, 3)
positions[6][1] = [0, 0, 2, 2]
positions[6][2] = [0, 2, 1, 1]
positions[6][3] = [1, 2, 1, 1]
positions[6][4] = [2, 2, 1, 1]
positions[6][6] = [2, 0, 1, 1]
positions[6][5] = [2, 1, 1, 1]

positions[7][0] = (4, 4)
positions[7][1] = [0, 0, 2, 2]
positions[7][2] = [0, 2, 2, 2]
positions[7][3] = [2, 2, 2, 2]
positions[7][4] = [2, 1, 1, 1]
positions[7][5] = [2, 0, 1, 1]
positions[7][6] = [3, 1, 1, 1]
positions[7][7] = [3, 0, 1, 1]

positions[7][1] = [0, 0, 2, 2]
positions[7][2] = [2, 0, 2, 2]
positions[7][3] = [0, 2, 2, 2]
positions[7][4] = [2, 2, 1, 1]
positions[7][5] = [3, 2, 1, 1]
positions[7][6] = [3, 3, 1, 1]
positions[7][7] = [2, 3, 1, 1]

positions[7][1] = [0, 0, 2, 2]
positions[7][2] = [0, 2, 2, 2]
positions[7][3] = [2, 1, 2, 2]
positions[7][4] = [2, 0, 1, 1]
positions[7][5] = [3, 0, 1, 1]
positions[7][6] = [3, 3, 1, 1]
positions[7][7] = [2, 3, 1, 1]

positions[8][0] = (4, 4)
positions[8][1] = [0, 0, 3, 3]
positions[8][2] = [0, 3, 1, 1]
positions[8][3] = [1, 3, 1, 1]
positions[8][4] = [2, 3, 1, 1]
positions[8][5] = [3, 3, 1, 1]
positions[8][6] = [3, 2, 1, 1]
positions[8][7] = [3, 1, 1, 1]
positions[8][8] = [3, 0, 1, 1]

positions[9][0] = (3, 3)
positions[9][1] = [0, 0, 1, 1]
positions[9][2] = [1, 0, 1, 1]
positions[9][3] = [0, 1, 1, 1]
positions[9][4] = [1, 1, 1, 1]
positions[9][5] = [0, 2, 1, 1]
positions[9][6] = [1, 2, 1, 1]
positions[9][7] = [2, 2, 1, 1]
positions[9][8] = [2, 1, 1, 1]
positions[9][9] = [2, 0, 1, 1]

positions[10][0] = (4, 4)
positions[10][1] = [0, 0, 2, 2]
positions[10][2] = [0, 2, 2, 2]
positions[10][3] = [2, 0, 1, 1]
positions[10][4] = [2, 1, 1, 1]
positions[10][5] = [2, 2, 1, 1]
positions[10][6] = [2, 3, 1, 1]
positions[10][7] = [3, 2, 1, 1]
positions[10][8] = [3, 3, 1, 1]
positions[10][9] = [3, 0, 1, 1]
positions[10][10] = [3, 1, 1, 1]

positions[10][0] = (4, 4)
positions[10][1] = [0, 0, 2, 2]
positions[10][2] = [0, 2, 2, 2]
positions[10][3] = [2, 0, 1, 1]
positions[10][4] = [3, 0, 1, 1]
positions[10][5] = [2, 1, 1, 1]
positions[10][6] = [3, 1, 1, 1]
positions[10][7] = [2, 2, 1, 1]
positions[10][8] = [3, 2, 1, 1]
positions[10][9] = [3, 3, 1, 1]
positions[10][10] = [2, 3, 1, 1]

positions[10][1] = [0, 0, 1, 1]
positions[10][2] = [1, 0, 1, 1]
positions[10][3] = [2, 0, 1, 1]
positions[10][4] = [3, 0, 1, 1]
positions[10][5] = [0, 1, 2, 2]
positions[10][6] = [2, 1, 2, 2]
positions[10][7] = [0, 3, 1, 1]
positions[10][8] = [1, 3, 1, 1]
positions[10][10] = [2, 3, 1, 1]
positions[10][9] = [3, 3, 1, 1]

positions[11][0] = (4, 4)
positions[11][1] = [1, 1, 2, 2]
positions[11][3] = [0, 0, 1, 1]
positions[11][2] = [1, 0, 1, 1]
positions[11][4] = [2, 3, 1, 1]
positions[11][5] = [2, 0, 1, 1]
positions[11][6] = [3, 3, 1, 1]
positions[11][7] = [3, 0, 1, 1]
positions[11][8] = [0, 3, 1, 1]
positions[11][9] = [1, 3, 1, 1]
positions[11][10] = [0, 1, 1, 2]
positions[11][11] = [3, 1, 1, 2]

positions[12][0] = (4, 4)
positions[12][1] = [1, 1, 2, 2]
positions[12][2] = [0, 0, 1, 1]
positions[12][3] = [1, 0, 1, 1]
positions[12][4] = [0, 1, 1, 1]
positions[12][5] = [2, 0, 1, 1]
positions[12][6] = [0, 2, 1, 1]
positions[12][7] = [3, 0, 1, 1]
positions[12][8] = [0, 3, 1, 1]
positions[12][9] = [1, 3, 1, 1]
positions[12][10] = [2, 3, 1, 1]
positions[12][11] = [3, 3, 1, 1]
positions[12][12] = [3, 1, 1, 2]

positions[13][0] = (4, 4)
positions[13][1] = [1, 1, 2, 2]
positions[13][2] = [0, 0, 1, 1]
positions[13][3] = [1, 0, 1, 1]
positions[13][4] = [0, 1, 1, 1]
positions[13][5] = [2, 0, 1, 1]
positions[13][6] = [0, 2, 1, 1]
positions[13][7] = [3, 0, 1, 1]
positions[13][8] = [0, 3, 1, 1]
positions[13][9] = [3, 1, 1, 1]
positions[13][10] = [1, 3, 1, 1]
positions[13][11] = [3, 2, 1, 1]
positions[13][12] = [2, 3, 1, 1]
positions[13][13] = [3, 3, 1, 1]

positions[16][0] = (4, 4)
positions[16][1] = [0, 0, 1, 1]
positions[16][2] = [1, 0, 1, 1]
positions[16][3] = [2, 0, 1, 1]
positions[16][4] = [0, 1, 1, 1]
positions[16][5] = [1, 1, 1, 1]
positions[16][6] = [2, 1, 1, 1]
positions[16][7] = [0, 2, 1, 1]
positions[16][8] = [1, 2, 1, 1]
positions[16][9] = [2, 2, 1, 1]
positions[16][10] = [3, 2, 1, 1]
positions[16][11] = [0, 3, 1, 1]
positions[16][12] = [1, 3, 1, 1]
positions[16][13] = [2, 3, 1, 1]
positions[16][14] = [3, 3, 1, 1]
positions[16][15] = [3, 1, 1, 1]
positions[16][16] = [3, 0, 1, 1]

with open(f'{path}json\\screens.json', 'w') as json_file:
    dump(positions, json_file)

from json import dump

# use pwd to get your path in the terminal
grid_order_fn = 'C:\\Users\\Jason\\Desktop\\python\\my-mvf1\\grid_order.json'



# make grid order list
commentary = {'F1 Live — MultiViewer': 'F1LIVE', 'International — MultiViewer': 'INT', 'Pit Lane — MultiViewer': 'PIT'}

drivers = {'Max Verstappen — MultiViewer': 'VER', 'Fernando Alonso — MultiViewer': 'ALO',
           'Sergio Perez — MultiViewer': 'PER', 'Lewis Hamilton — MultiViewer': 'HAM',
           'Charles Leclerc — MultiViewer': 'LEC', 'George Russell — MultiViewer': 'RUS',
           'Carlos Sainz — MultiViewer': 'SAI', 'Lance Stroll — MultiViewer': 'STR',
           'Lando Norris — MultiViewer': 'NOR', 'Kevin Magnussen — MultiViewer': 'MAG',
           'Esteban Ocon — MultiViewer': 'OCO', 'Nico Hulkenberg — MultiViewer': 'HUL',
           'Valtteri Bottas — MultiViewer': 'BOT', 'Alexander Albon — MultiViewer': 'ALB',
           'Yuki Tsunoda — MultiViewer': 'TSU', 'Guanyu Zhou — MultiViewer': 'ZHO',
           'Pierre Gasly — MultiViewer': 'GAS', 'Nyck De Vries — MultiViewer': 'DEV',
           'Oscar Piastri — MultiViewer': 'PIA', 'Logan Sargeant — MultiViewer': 'SAR',
           'Sebastian Vettel — MultiViewer': 'VET', 'Mick Schumacher — MultiViewer': 'MSC',
           'Daniel Ricciardo — MultiViewer': 'RIC', 'Nicholas Latifi — MultiViewer': 'LAT',
           'Liam Lawson — MultiViewer': 'LAW', 'Kimi Räikkönen — MultiViewer': 'RAI',
           'Robert Kubica — MultiViewer': 'KUB', 'Daniil Kvyat — MultiViewer': 'KVY',
           'Antonio Giovinazzi — MultiViewer': 'GIO', 'Romain Grosjean — MultiViewer': 'GRO',
           'Nikita Mazepin — MultiViewer': 'MAZ',
           'Marcus Ericsson — MultiViewer': 'ERI',
           'Sergey Sirotkin — MultiViewer': 'SIR',
           'Brendon Hartley — MultiViewer': 'HAR',
           'Stoffel Vandoorne — MultiViewer': 'VAN'}

data = {'Data Channel — MultiViewer': 'DATA', 'Driver Tracker — MultiViewer': 'TRACKER'}

all = commentary.copy()
all.update(drivers)
all.update(data)

all_list = list(all.keys())


print('arrange_players.py')
print("grid_order_fn = '"+grid_order_fn.replace('\\','\\\\')+"'")
print('all_list = ' + str(all_list))



swapped_drivers = {value: key for key, value in drivers.items()}
print()
print('toggle_driver.py')
print("grid_order_fn = '"+grid_order_fn.replace('\\','\\\\')+"'")
print('drivers = ' + str(swapped_drivers))


grid_order = drivers.copy()
grid_order.update(data)

x = list(grid_order.keys())

# save those dictionaries
with open(grid_order_fn, 'w') as json_file:
    dump(x, json_file, indent=4)



positions = [[None for _ in range(25)] for _ in range(25)]

positions[1][0] = (1, 1)
positions[1][1] = [0, 0, 1, 1]

positions[2][0] = (1, 2)
positions[2][1] = [0, 1, 1, 1]
positions[2][2] = [0, 0, 1, 1]

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

positions[11][1] = [0, 0, 2, 2]
positions[11][2] = [2, 0, 1, 1]
positions[11][3] = [3, 0, 1, 1]
positions[11][4] = [2, 1, 1, 1]
positions[11][5] = [3, 1, 1, 1]
positions[11][6] = [0, 2, 1, 2]
positions[11][7] = [1, 2, 1, 2]
positions[11][8] = [2, 2, 1, 1]
positions[11][9] = [2, 3, 1, 1]
positions[11][10] = [3, 3, 1, 1]
positions[11][11] = [3, 2, 1, 1]

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

positions[14][0] = (4, 4)
positions[14][1] = [1, 0, 1, 1]
positions[14][2] = [2, 0, 1, 1]
positions[14][3] = [3, 0, 1, 1]
positions[14][4] = [1, 1, 1, 1]
positions[14][5] = [2, 1, 1, 1]
positions[14][6] = [3, 1, 1, 1]
positions[14][7] = [1, 2, 1, 1]
positions[14][8] = [2, 2, 1, 1]
positions[14][9] = [3, 2, 1, 1]
positions[14][10] = [1, 3, 1, 1]
positions[14][11] = [2, 3, 1, 1]
positions[14][12] = [3, 3, 1, 1]
positions[14][13] = [0, 2, 1, 2]
positions[14][14] = [0, 0, 1, 2]

positions[15][0] = (4, 4)
positions[15][1] = [0, 0, 1, 1]
positions[15][2] = [0, 1, 1, 1]
positions[15][3] = [1, 0, 1, 1]
positions[15][4] = [1, 1, 1, 1]
positions[15][5] = [1, 2, 1, 1]
positions[15][6] = [2, 0, 1, 1]
positions[15][7] = [2, 1, 1, 1]
positions[15][8] = [2, 2, 1, 1]
positions[15][9] = [2, 3, 1, 1]
positions[15][10] = [3, 0, 1, 1]
positions[15][11] = [3, 1, 1, 1]
positions[15][12] = [3, 2, 1, 1]
positions[15][13] = [3, 3, 1, 1]
positions[15][14] = [1, 3, 1, 1]
positions[15][15] = [0, 2, 1, 2]

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

print()
print('tiler.py')
print('positions = ' + str(positions))

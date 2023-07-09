from bs4 import BeautifulSoup
import csv

path = r'/home/jovyan/Formula 1/data/'

# Driver
html_file = path + r'drivers.html'
with open(html_file) as soup_file:
    soup = BeautifulSoup(soup_file, 'html.parser')

table = soup.find('table')
trs = table.findAll('tr')
trs_count = len(trs)

driver_standings = {}
for i in range(1, trs_count):
    spans = trs[i].findAll('span')
    driver_standings[spans[2].get_text()] = i - 1

driver_standings_keys = list(driver_standings.keys())
driver_standings_keys.sort()

# Team
html_file = path + r'teams.html'

with open(html_file) as soup_file:
    soup = BeautifulSoup(soup_file, 'html.parser')
table = soup.find('tbody')
trs = table.findAll('tr')

team_standings = {}
for inx, tr in enumerate(trs):
    a = tr.find('a')
    team_standings[a.get_text()] = inx

team_standings_keys = list(team_standings.keys())
team_standings_keys.sort()

csv_file = r'/home/jovyan/Formula 1/data/predictions.csv'
with open(csv_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    rows = []
    for row in csv_reader:
        rows.append(row)

w, h = 6, 10

# Team
team_rows = [[0 for x in range(w)] for y in range(h)]

for x in range(10):
    j = x + 2
    for y in range(6):
        i = y + 6
        if rows[j][i] == '':
            team_rows[x][y] = ''
        else:
            team_rows[x][y] = rows[j][i]

# Driver
driver_rows = [[0 for x in range(w)] for y in range(h)]

for x in range(10):
    j = x + 15
    for y in range(6):
        i = y + 6
        if rows[j][i] == '':
            driver_rows[x][y] = ''
        else:
            driver_rows[x][y] = rows[j][i]

points_array = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

# Team
team_list = {'Alfa Romeo': 'Alfa Romeo Ferrari', 'Alfa Tauri': 'AlphaTauri Honda RBPT',
             'Alpha Romeo': 'Alfa Romeo Ferrari', \
             'Alpha Tauri': 'AlphaTauri Honda RBPT', 'Alpine': 'Alpine Renault', 'Aston Martin': 'Alpine Renault',
             'Austin': 'Alpine Renault', \
             'F': 'Ferrari', 'Ferarri': 'Ferrari', 'Ferrari': 'Ferrari', 'Haas': 'Haas Ferrari',
             'McLaren': 'McLaren Mercedes', 'Merc': 'Mercedes', \
             'Mercedes ': 'Mercedes', 'Mercedes': 'Mercedes', 'RB': 'Red Bull Racing Honda RBPT',
             'Red Bull': 'Red Bull Racing Honda RBPT', \
             'Williams': 'Williams Mercedes', 'Mclaren': 'McLaren Mercedes', 'AlphaTauri': 'AlphaTauri Honda RBPT',
             'Alpine F1 Team': 'Alpine Renault', \
             'Haas F1 Team': 'Haas Ferrari'}

team_list_keys = list(team_list.keys())
team_list_keys.sort()

# Driver
driver_list = {'Alonso': 'ALO', 'Battery Voltas': 'BOT', 'Botas': 'BOT', 'Bottas': 'BOT', 'Bottox': 'BOT',
               'Falonzio': 'ALO', 'Hamilton': 'HAM', \
               'Hamilton ': 'HAM', 'Hulkenberg': 'HUL', 'Lando': 'NOR', 'LeClerc': 'LEC', 'Leclerc': 'LEC',
               'Mag': 'MAG', 'Norris': 'NOR', \
               'Ocon': 'OCO', 'Perez': 'PER', 'Russel': 'RUS', 'Russell': 'RUS', 'Sainz': 'SAI', 'Stroll': 'STR',
               'Tsunoda': 'TSU', 'Ver': 'VER', \
               'Verstappen': 'VER', 'Versteppen': 'VER', 'Zhou': 'ZHO', 'ham': 'HAM', 'lec': 'LEC', 'per': 'PER',
               'rus': 'RUS', 'sai': 'SAI', \
               'Super Max': 'VER', 'Chico': 'PER', 'Chuck': 'LEC', 'Hammer Time': 'HAM', 'inSainz': 'SAI',
               'Rustler': 'RUS', 'Stroller': 'STR', \
               'Gasman': 'GAS', 'Max': 'VER', 'Buttocks': 'BOT', 'Ham Bone': 'HAM', 'Hülkenberg': 'HUL', 'Gasly': 'GAS'}

driver_list_keys = list(driver_list.keys())
driver_list_keys.sort()

# print team names that aren't in the dictionary

for j in range(6, 12):
    for i in range(2, 12):
        if rows[i][j] != '' and rows[i][j] not in team_list_keys:
            print(f", '{rows[i][j]}':''", end='')
print()
print()

# print driver names that aren't in the dictionary

for j in range(6, 12):
    for i in range(15, 25):
        if rows[i][j] != '' and rows[i][j] not in driver_list_keys:
            print(f", '{rows[i][j]}':''", end='')

# Team
csv_file = r'/home/jovyan/Formula 1/points.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(['Jason', '', '', 'Bella', '', '', 'Cole', '', '', 'Kyle', '', '', 'Kelly', '', '', 'Rune', ''])

    team_points = [0, 0, 0, 0, 0, 0]
    for x in range(10):
        row = []

        for y in range(6):
            # print(team_rows[x][y])
            if team_rows[x][y] != '' and team_rows[x][y] in team_list_keys:
                pick = team_list[team_rows[x][y]]
                if pick in team_standings_keys:
                    pick_standings = team_standings[pick]
                    diff = abs(x - pick_standings)
                    if diff <= 9:
                        points = points_array[diff]
                    else:
                        points = 0
                else:
                    points = 0
            else:
                pick = ''
                points = 0

            team_points[y] = team_points[y] + points

            row.append(team_rows[x][y])
            row.append(points)
            row.append('')

        writer.writerow(row)
    row = []
    for val in team_points:
        row.append('')
        row.append(val)
        row.append('')

    writer.writerow(row)
    writer.writerow('')
    writer.writerow('')

    # Drivers

    driver_points = [0, 0, 0, 0, 0, 0]
    for x in range(10):
        row = []

        for y in range(6):
            # print(driver_rows[x][y])
            if driver_rows[x][y] != '' and driver_rows[x][y] in driver_list_keys:
                pick = driver_list[driver_rows[x][y]]
                if pick in driver_standings_keys:
                    pick_standings = driver_standings[pick]
                    diff = abs(x - pick_standings)
                    if diff <= 9:
                        points = points_array[diff]
                    else:
                        points = 0
                else:
                    points = 0
            else:
                pick = ''
                points = 0

            if pick in driver_standings_keys:
                pick_standings = driver_standings[pick]
            else:
                pick_standings = 30

            # print(f'\t{driver_rows[x][y]:4}\t{points:3}\t', end='')

            driver_points[y] = driver_points[y] + points

            row.append(driver_rows[x][y])
            row.append(points)
            row.append('')

        writer.writerow(row)
    row = []
    for val in driver_points:
        row.append('')
        row.append(val)
        row.append('')

    writer.writerow(row)




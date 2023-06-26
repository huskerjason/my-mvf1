import json
import sys
import arrange_players





grid_order_fn = 'C:\\Users\\Jason\\Desktop\\python\\my-mvf1\\grid_order.json'
drivers = {'VER': 'Max Verstappen — MultiViewer', 'ALO': 'Fernando Alonso — MultiViewer', 'PER': 'Sergio Perez — MultiViewer', 'HAM': 'Lewis Hamilton — MultiViewer', 'LEC': 'Charles Leclerc — MultiViewer', 'RUS': 'George Russell — MultiViewer', 'SAI': 'Carlos Sainz — MultiViewer', 'STR': 'Lance Stroll — MultiViewer', 'NOR': 'Lando Norris — MultiViewer', 'MAG': 'Kevin Magnussen — MultiViewer', 'OCO': 'Esteban Ocon — MultiViewer', 'HUL': 'Nico Hulkenberg — MultiViewer', 'BOT': 'Valtteri Bottas — MultiViewer', 'ALB': 'Alexander Albon — MultiViewer', 'TSU': 'Yuki Tsunoda — MultiViewer', 'ZHO': 'Guanyu Zhou — MultiViewer', 'GAS': 'Pierre Gasly — MultiViewer', 'DEV': 'Nyck De Vries — MultiViewer', 'PIA': 'Oscar Piastri — MultiViewer', 'SAR': 'Logan Sargeant — MultiViewer', 'VET': 'Sebastian Vettel — MultiViewer', 'MSC': 'Mick Schumacher — MultiViewer', 'RIC': 'Daniel Ricciardo — MultiViewer', 'LAT': 'Nicholas Latifi — MultiViewer', 'LAW': 'Liam Lawson — MultiViewer', 'RAI': 'Kimi Räikkönen — MultiViewer', 'KUB': 'Robert Kubica — MultiViewer', 'KVY': 'Daniil Kvyat — MultiViewer', 'GIO': 'Antonio Giovinazzi — MultiViewer', 'GRO': 'Romain Grosjean — MultiViewer', 'MAZ': 'Nikita Mazepin — MultiViewer', 'ERI': 'Marcus Ericsson — MultiViewer', 'SIR': 'Sergey Sirotkin — MultiViewer', 'HAR': 'Brendon Hartley — MultiViewer', 'VAN': 'Stoffel Vandoorne — MultiViewer'}

def move_driver_up(tlc):
    with open(grid_order_fn, 'r') as json_file:
        list1 = json.load(json_file)
    if drivers[tlc] in list1:
        index = list1.index(drivers[tlc])
        list1.insert(0, list1.pop(index))
        with open(grid_order_fn, 'w') as json_file:
            json.dump(list1, json_file, indent=4)


if __name__ == "__main__":

    if sys.argv:
        if len(sys.argv) >= 2:
            x = sys.argv[1]
            move_driver_up(x)
        else:
            move_driver_up('BOT')
    arrange_players.arrange()
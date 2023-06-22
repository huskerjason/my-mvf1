import sys

import json


def move_to_top(driver_tlc):
    with open(r'C:/Users/Jason/Desktop/python/MultiViewer_Formula_1/json/drivers.json', 'r') as json_file:
        player_dict = json.load(json_file)

    # Iterate through the dictionary and find the key associated with the desired value
    in_dict = False
    for key, val in player_dict.items():
        if val == driver_tlc:
            in_dict = True
            break  # Exit the loop once the key is found

    if in_dict:
        new_dict = {key: val}
        for key, val in player_dict.items():
            if val != driver_tlc:
                new_dict.update({key: val})
    else:
        return

    with open(r'C:/Users/Jason/Desktop/python/MultiViewer_Formula_1/json/drivers.json', 'w') as json_file:
        # dump(player_driver_dict, json_file, indent=4)
        json.dump(new_dict, json_file, indent=4)


if __name__ == "__main__":

    if sys.argv:
        if len(sys.argv) >= 2:
            x = sys.argv[1]
            move_to_top(x)


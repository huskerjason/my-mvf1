import json
from math import sqrt

import win32con
import win32gui


# import json
with open('json\\drivers.json', 'r') as json_file:
    player_dict = json.load(json_file)
with open('json\\screens.json', 'r') as json_file:
    positions = json.load(json_file)


def get_window_info(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    x, y, width, height = left, top, right - left, bottom - top
    title = win32gui.GetWindowText(hwnd)
    return {
        "Title": title,
        "Position": (x, y),
        "Size": (width, height)
    }


def list_all_windows():
    windows = []

    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            x = get_window_info(hwnd)
            if x['Title'] in player_dict.keys():
                windows.append(x)

    win32gui.EnumWindows(callback, windows)
    return windows


def sqrt_close(i):
    x = sqrt(i)
    x_int = int(x)
    if x == x_int:
        return x_int
    else:
        return x_int + 1


def unmax(title):
    print(title)
    hwnd = win32gui.FindWindow(None, title)
    print(get_window_info(hwnd))


def check_min_max():
    win_list = get_win_list()
    for win in win_list:
        if win['Position'] == (-32000, -32000):
            hwnd = win32gui.FindWindow(None, win['Title'])
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win_list = get_win_list()
    for win in win_list:
        print(win['Title'], win['Size'])

        if win['Size'][0] >= 1915 and win['Size'][0] >= 1075:
            print('  ' + win['Title'], win['Size'])
            hwnd = win32gui.FindWindow(None, win['Title'])
            # win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

            # unmax(win['Title'])


def get_win_list():
    window_list = []
    window_list_temp = list_all_windows()
    for p in player_dict:
        for w in window_list_temp:
            if p in w['Title']:
                window_list.append(w)
    return window_list


if __name__ == "__main__":

    # print(player_dict,type(player_dict))

    window_list = get_win_list()
    check_min_max()

    window_list = get_win_list()

    count = len(window_list)
    if count <= 3:
        pass



    elif count <= 9:
        for inx, w in enumerate(window_list):
            # print(count, inx, w['Title'], positions[count][inx])

            x, y, width, height = positions[count][inx]

            hwnd = win32gui.FindWindow(None, w['Title'])
            win32gui.SetWindowPos(hwnd, 0, x, y, width, height, 0)



    elif count <= 25:
        grid_size = sqrt_close(count)
        width = int(1820 / grid_size)
        height = int(width * 9 / 16)
        h = int(1039 / grid_size)
        if h < height:
            width = int(h * 16 / 9)
            height = h

        print(count, width, height)

        for i in range(count):
            row = int(i / grid_size)
            col = i % grid_size

            x = col * width - 1920
            y = row * height

            print(window_list[i]['Title'])
            hwnd = win32gui.FindWindow(None, window_list[i]['Title'])
            win32gui.SetWindowPos(hwnd, 0, x, y, width, height, 0)



    else:
        pass

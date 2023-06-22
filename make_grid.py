import json
from math import sqrt

import win32gui

with open(r'bats/arrange.bat', 'r') as json_file:
    player_dict = json.load(json_file)


def get_window_info(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    x, y, width, height = left, top, right - left, bottom - top
    title = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)
    return {
        "Title": title,
        "Class Name": class_name,
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


if __name__ == "__main__":

    window_list = list_all_windows()
    count = len(window_list)

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

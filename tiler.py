from math import sqrt
from time import sleep

import json
import win32con
import win32gui


def sqrt_close(i):
    x = sqrt(i)
    x_int = int(x)
    if x == x_int:
        return x_int
    else:
        return x_int + 1


def get_window_info(hwnd):
    left1, top1, right1, bottom1 = win32gui.GetWindowRect(hwnd)
    x, y, width, height = left1, top1, right1 - left1, bottom1 - top1
    title = win32gui.GetWindowText(hwnd)
    return {
        "Title": title,
        "Position": (x, y),
        "Size": (width, height),
        "hwnd": hwnd
    }


def windows_list():
    with open('./json/drivers.json', 'r') as json_file:
        player_dict1 = json.load(json_file)

    def callback_windows_list(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            x = get_window_info(hwnd)
            if x['Title'] in player_dict1.keys():
                windows.append(x)

    windows_list = []
    win32gui.EnumWindows(callback_windows_list, windows_list)

    return windows_list


def get_hwnds():
    with open('./json/drivers.json', 'r') as json_file:
        player_dict2 = json.load(json_file)

    # close any duplicate players

    unique = []
    close_timer = 0
    for w in windows_list():
        if w['Title'] in unique:
            print(w['hwnd'])
            win32gui.PostMessage(w['hwnd'], win32con.WM_CLOSE, 0, 0)
            close_timer += .1
        else:
            unique.append(w['Title'])
    sleep(close_timer)

    print(unique)
    print(windows_list())
    the_list = []
    for player in player_dict2:
        if player in unique:
            for win in windows_list():
                if win['Title'] == player:
                    print(player)
                    the_list.append(win['hwnd'])
                    break
    return the_list


def tiler(hwnd_list, left, top, right, bottom):

    # get the left top cornor coords
    x = left if left < right else right  # and check that the top is the top
    y = top if top < bottom else bottom

    # get width and heigth
    total_width = abs(right - left)
    total_heigth = abs(bottom - top)


    count = len(hwnd_list)
    print('Count: ' + str(count))
    if count == 0:
        return


    with open(r'./json/screens.json', 'r') as json_file:
        positions = json.load(json_file)


    if count <= 13 or count == 16:

        grid_width, grid_height = positions[count][0]
        width_player = int(total_width / grid_width)
        height_player = int(total_heigth / grid_height)

        grid_size = sqrt_close(count)
        width = int(1820 / grid_size)
        height = int(width * 9 / 16)
        h = int(1039 / grid_size)
        if h < height:
            width = int(h * 16 / 9)
            height = h


        for inx, hwnd in enumerate(hwnd_list):

            xx, yy, ww, hh = positions[count][inx + 1]

            x = xx * width_player + left
            y = yy * height_player + top
            w = ww * width_player
            h = hh * height_player

            try:

                win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                # win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                # win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                # win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                win32gui.SetWindowPos(hwnd, 0, x, y, w, h, 0)
                print(x, y)

            except:
                pass



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

            print(hwnd_list[i])
            win32gui.SetWindowPos(hwnd_list[i], 0, x, y, width, height, 0)

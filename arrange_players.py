from time import sleep

import json
import tiler
import win32con
import win32gui

# left, top, right and bottom
ll = -1920
tt = 0
rr = 2
bb = 1042

ll = -1918
tt = 2
rr = -2
bb = 1038

path = 'C:\\Users\\Jason\\Desktop\\python\\jch-mvf1\\Main\\'

def windows_list(json_fn='drivers'):
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
    with open(f'{path}json\{json_fn}.json', 'r') as json_file:
        dict1 = json.load(json_file)

    def callback_windows_list(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            x = get_window_info(hwnd)
            if x['Title'] in dict1.keys():
                windows.append(x)

    windows_list = []
    win32gui.EnumWindows(callback_windows_list, windows_list)

    return windows_list


def get_hwnds():

    unique = []
    close_timer = 0
    for w in windows_list('all'):
        if w['Title'] in unique:
            print(w['hwnd'])
            win32gui.PostMessage(w['hwnd'], win32con.WM_CLOSE, 0, 0)
            close_timer += .1
        else:
            unique.append(w['Title'])
    sleep(close_timer)

    with open(f'{path}json\drivers.json', 'r') as json_file:
        player_dict2 = json.load(json_file)
    the_list = []
    for player in player_dict2:
        if player in unique:
            for win in windows_list():
                if win['Title'] == player:
                    the_list.append(win['hwnd'])
                    break
            # break
    return the_list


if __name__ == "__main__":
    # ll = -1920
    # tt = 0
    # rr = 2
    # bb = 1042


    hwnds = get_hwnds()

    # print(hwnds)


    tiler.tiler(hwnd_list=hwnds, left=ll, top=tt, right=rr, bottom=bb)

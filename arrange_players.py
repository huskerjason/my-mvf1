import json
from time import sleep

import pyautogui
import win32con
import win32gui

import tiler

grid_order_fn = 'C:\\Users\\Jason\\Desktop\\python\\my-mvf1\\grid_order.json'
all_list = ['F1 Live — MultiViewer', 'International — MultiViewer', 'Pit Lane — MultiViewer', 'Max Verstappen — MultiViewer', 'Fernando Alonso — MultiViewer', 'Sergio Perez — MultiViewer', 'Lewis Hamilton — MultiViewer', 'Charles Leclerc — MultiViewer', 'George Russell — MultiViewer', 'Carlos Sainz — MultiViewer', 'Lance Stroll — MultiViewer', 'Lando Norris — MultiViewer', 'Kevin Magnussen — MultiViewer', 'Esteban Ocon — MultiViewer', 'Nico Hulkenberg — MultiViewer', 'Valtteri Bottas — MultiViewer', 'Alexander Albon — MultiViewer', 'Yuki Tsunoda — MultiViewer', 'Guanyu Zhou — MultiViewer', 'Pierre Gasly — MultiViewer', 'Nyck De Vries — MultiViewer', 'Oscar Piastri — MultiViewer', 'Logan Sargeant — MultiViewer', 'Sebastian Vettel — MultiViewer', 'Mick Schumacher — MultiViewer', 'Daniel Ricciardo — MultiViewer', 'Nicholas Latifi — MultiViewer', 'Liam Lawson — MultiViewer', 'Kimi Räikkönen — MultiViewer', 'Robert Kubica — MultiViewer', 'Daniil Kvyat — MultiViewer', 'Antonio Giovinazzi — MultiViewer', 'Romain Grosjean — MultiViewer', 'Nikita Mazepin — MultiViewer', 'Marcus Ericsson — MultiViewer', 'Sergey Sirotkin — MultiViewer', 'Brendon Hartley — MultiViewer', 'Stoffel Vandoorne — MultiViewer', 'Jack Aitken — MultiViewer', 'Pietro Fittipaldi — MultiViewer', 'Data Channel — MultiViewer', 'Driver Tracker — MultiViewer']


# left, top, right and bottom
ll = -1920
tt = 0
rr = 2
bb = 1042

ll = -1918
tt = 2
rr = -2
bb = 1038


def windows_list(json_fn='drivers'):
    if json_fn == 'drivers':
        with open(grid_order_fn, 'r') as json_file:
            list1 = json.load(json_file)
    elif json_fn == 'all':
        list1 = all_list

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

    def callback_windows_list(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            x = get_window_info(hwnd)
            if x['Title'] in list1:
                windows.append(x)

    windows_list = []
    win32gui.EnumWindows(callback_windows_list, windows_list)
    return windows_list


def get_hwnds():
    unique = []
    close_timer = 0
    win_list = windows_list('all')
    win_list.reverse()
    for w in win_list:
        if w['Title'] in unique:
            print(w['hwnd'])
            win32gui.PostMessage(w['hwnd'], win32con.WM_CLOSE, 0, 0)
            close_timer += .1
        else:
            unique.append(w['Title'])
    sleep(close_timer)

    with open(grid_order_fn, 'r') as json_file:
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


def sync_players():
    hwnd = win32gui.FindWindow(None, 'F1 Live — MultiViewer')
    if not hwnd:
        hwnd = win32gui.FindWindow(None, 'International — MultiViewer')
        if not hwnd:
            hwnd = win32gui.FindWindow(None, 'Pit Lane — MultiViewer')

    if hwnd:
        print(hwnd)

        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)

        left, top, right, bottom = win32gui.GetWindowRect(hwnd)

        x = int((left + right) / 2)
        y = int((top + bottom) / 2)

        pos = pyautogui.position()
        pyautogui.moveTo(x, y)
        pyautogui.click(x, y)
        pyautogui.keyDown('s')
        pyautogui.keyUp('s')
        pyautogui.moveTo(pos)


def arrange():
    sync_players()
    hwnds = get_hwnds()
    tiler.tiler(hwnd_list=hwnds, left=ll, top=tt, right=rr, bottom=bb)


if __name__ == "__main__":
    arrange()

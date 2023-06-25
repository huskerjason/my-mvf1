from time import sleep

import sys

import win32gui


def replay_live_timing():
    # the timing player can have 1 of 2 titles, try them and see if they exist
    hwnd = win32gui.FindWindow(None, 'Replay Live Timing — MultiViewer')
    if hwnd:
        win32gui.SetWindowPos(hwnd, 0, -7, -50, 1, 1200, 0)
    else:
        hwnd = win32gui.FindWindow(None, 'Live Timing — MultiViewer')
        if hwnd:
            win32gui.SetWindowPos(hwnd, 0, -7, -50, 1, 1200, 0)


def player_launch_menu(size='big'):
    # return
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)

            if 'MultiViewer' in title:
                if any(word in title for word in ['2023', '2022', '2021', '2020', '2019', '2018', 'Home']):
                    windows.append({"title": title, "hwnd": hwnd})
            elif title == 'MultiViewer':
                windows.append({"title": title, "hwnd": hwnd})

    players = []
    win32gui.EnumWindows(callback, players)
    if players:
        hwnd = players[0]['hwnd']
        if hwnd:
            win32gui.SetWindowPos(hwnd, 0, 1024, 0, 0, 1020, 0)


def commentary(size='big'):
    hwnd_f1live = win32gui.FindWindow(None, 'F1 Live — MultiViewer')
    hwnd_int = win32gui.FindWindow(None, 'International — MultiViewer')
    hwnd_pit = win32gui.FindWindow(None, 'Pit Lane — MultiViewer')



    if size in ['big']:
        if hwnd_f1live:
            win32gui.SetWindowPos(hwnd_f1live, 0, 103, 2, 1806, 1016, 0)
        elif hwnd_int:
            win32gui.SetWindowPos(hwnd_int, 0, 103, 2, 1806, 1016, 0)
        elif hwnd_pit:
            win32gui.SetWindowPos(hwnd_pit, 0, 103, 2, 1806, 1016, 0)


    elif size in ['small']:
        if hwnd_f1live:
            win32gui.SetWindowPos(hwnd_f1live,0, 98, 1, 1280, 720, 0)
            if hwnd_int:
                win32gui.SetWindowPos(hwnd_int,0, 129, 726, 553, 311, 0)
        elif hwnd_int:
            win32gui.SetWindowPos(hwnd_int,0, 98, 1, 1280, 720, 0)
            if hwnd_pit:
                win32gui.SetWindowPos(hwnd_pit,0, 129, 726, 553, 311, 0)
        elif hwnd_pit:
            win32gui.SetWindowPos(hwnd_pit,0, 98, 1, 1280, 720, 0)




    elif size in ['pycharm']:
        if hwnd_f1live:
            win32gui.SetWindowPos(hwnd_f1live,0, 123, 1, 644, 362, 0)
            if hwnd_int:
                win32gui.SetWindowPos(hwnd_int,0, 769, 1, 644, 362, 0)
        elif hwnd_int:
            win32gui.SetWindowPos(hwnd_int,0, 123, 1, 644, 362, 0)
            if hwnd_pit:
                win32gui.SetWindowPos(hwnd_pit,0, 769, 1, 644, 362, 0)
        elif hwnd_pit:
            win32gui.SetWindowPos(hwnd_pit,0, 123, 1, 644, 362, 0)









if __name__ == "__main__":



    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)

            if 'MultiViewer' in title:
                if any(word in title for word in ['2023', '2022', '2021', '2020', '2019', '2018', 'Home']):
                    windows.append({"title": title, "hwnd": hwnd})
            elif title == 'MultiViewer':
                windows.append({"title": title, "hwnd": hwnd})
    players = []
    win32gui.EnumWindows(callback, players)



    def all_three(var=None):
        replay_live_timing()
        player_launch_menu(var)
        commentary(var)


    if len(sys.argv) >= 2:
        all_three(sys.argv[1])
    else:
        all_three()

import sys
import win32gui

#

def replay_live_timing(left, top, width, heigth):
    # the timing player can have 1 of 2 titles, try them and see if they exist
    hwnd = win32gui.FindWindow(None, 'Replay Live Timing — MultiViewer')
    if hwnd:
        win32gui.SetWindowPos(hwnd, 0, left, top, width, heigth, 0)
    else:
        hwnd = win32gui.FindWindow(None, 'Live Timing — MultiViewer')
        if hwnd: win32gui.SetWindowPos(hwnd, 0, left, top, width, heigth, 0)


def player_launch_menu(left=1024, top=0, width=0, heigth=0):

    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if ' — MultiViewer' in title:
                if '2023' in title or '2022' in title or 'Home' in title:
                    windows.append({"title": title, "hwnd": hwnd})
            elif title =='MultiViewer':
                windows.append({"title": title, "hwnd": hwnd})

    players = []
    win32gui.EnumWindows(callback, players)
    if players:
        hwnd = players[0]['hwnd']
        if hwnd:
            win32gui.SetWindowPos(hwnd, 0, left, top, width, heigth, 0)


def commentary(left, top, width, heigth):
    hwnd = win32gui.FindWindow(None, 'F1 Live — MultiViewer')
    if hwnd:
        win32gui.SetWindowPos(hwnd, 0, left, top, width, heigth, 0)
        hwnd_intl = win32gui.FindWindow(None, 'International — MultiViewer')
        if hwnd_intl:
            win32gui.SetWindowPos(hwnd_intl, 0, left + 20, top + 20, width + 20, heigth + 20, 0)

    else:
        hwnd = win32gui.FindWindow(None, 'International — MultiViewer')
        if hwnd:
            win32gui.SetWindowPos(hwnd, 0, left, top, width, heigth, 0)


if __name__ == "__main__":

    if len(sys.argv) >= 2:
        if sys.argv[1] in ['Left', 'left', 'l', 'L']:
            replay_live_timing(-1926, 1, 0, 1046)
        elif sys.argv[1] in ['Right', 'right', 'r', 'R']:
            replay_live_timing(-106, 1, 1, 1046)
        elif sys.argv[1] in ['small']:
            player_launch_menu(1024, 0, 0, 1020)
            replay_live_timing(-7, -50, 1, 1200)
            commentary(98, 1, 1280, 720)
        elif sys.argv[1] in ['big']:
            replay_live_timing(-7, -50, 1, 1200)
            commentary(103, 2, 1806, 1016)

    else:
        replay_live_timing(-7, -50, 1, 1100)
        commentary(98, 1, 1280, 720)
        player_launch_menu(1024, 0, 0, 1020)

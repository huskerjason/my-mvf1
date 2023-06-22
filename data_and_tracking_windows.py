import win32gui


def place_window(channel, left, top, right, bottom):
    hwnd = win32gui.FindWindow(None, channel)
    print(hwnd)
    if hwnd:
        win32gui.SetWindowPos(hwnd, 0, left, top, right, bottom, 0)


# Driver Tracker — MultiViewer


if __name__ == "__main__":
    place_window('Data Channel — MultiViewer', -375, -110, 1600, 900)

    left = -420
    top = 625
    right = 50
    bottom = 1040
    width = abs(left-right)
    heigth = abs(top-bottom)

    place_window('Driver Tracker — MultiViewer', left,top, width, heigth)

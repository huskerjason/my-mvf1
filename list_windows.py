import win32gui


def get_player_lauch_menu_handle():
    def get_window_info(hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        x, y, width, height = left, top, right - left, bottom - top
        title = win32gui.GetWindowText(hwnd)
        return {"title": title, "hwnd": hwnd}

    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            x = get_window_info(hwnd)
            if '2023' in x['title'] and ' — MultiViewer' in x['title']:
                # if ' — MultiViewer' in x['title']:
                windows.append(x)

    windows = []
    win32gui.EnumWindows(callback, windows)
    if len(windows):
        return windows[0]['hwnd']


def list_all_windows():
    #

    def get_window_info(hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        x, y, width, height = left, top, right - left, bottom - top
        title = win32gui.GetWindowText(hwnd)
        return {
            "title": title,
            "hwnd": hwnd,
            "pos": ((x, y), (width, height))
        }

    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            x = get_window_info(hwnd)
            if 1 or ' — MultiViewer' in x['title']:
                windows.append(x)

    windows = []

    win32gui.EnumWindows(callback, windows)
    return windows


if __name__ == "__main__":

    for w in list_all_windows():
        print(w)

    print(get_player_lauch_menu_handle())
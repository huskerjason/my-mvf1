import win32gui

all_windows = 0


def list_all_windows():
    #

    def get_window_info(hwnd):
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        x, y, width, height = left, top, right - left, bottom - top
        title = win32gui.GetWindowText(hwnd)
        class1 = win32gui.GetClassName(hwnd)

        return {"title": title, "hwnd": hwnd, 'class': class1, "pos": [x, y, width, height]}

    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            x = get_window_info(hwnd)
            if all_windows or ' — MultiViewer' in x['title']:
                windows.append(x)

    windows = []

    win32gui.EnumWindows(callback, windows)
    return windows


if __name__ == "__main__":

    for w in list_all_windows():
        if 1:
            print(f"'{w['title']}': '',")
        elif 1:
            print(f"{w['class']:40} {w['title']:40} {w['pos']}")
        else:
            print(w)


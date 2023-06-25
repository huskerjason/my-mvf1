import pyautogui
import win32con
import win32gui


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


if __name__ == "__main__":
    sync_players()

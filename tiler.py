from math import sqrt

import win32con
import win32gui


def tiler(hwnd_list, left, top, right, bottom):
    # get the left top corner coords
    x = left if left < right else right  # and check that the top is the top
    y = top if top < bottom else bottom

    # get width and heigth
    total_width = abs(right - left)
    total_heigth = abs(bottom - top)

    count = len(hwnd_list)
    print('Count: ' + str(count))
    if not count: return

    positions = [
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [(1, 1), [0, 0, 1, 1], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None],
        [(1, 2), [0, 0, 1, 1], [0, 1, 1, 1], None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None],
        [(2, 2), [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 2, 1], None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None],
        [(2, 2), [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None],
        [(5, 6), [0, 0, 3, 3], [0, 3, 3, 3], [3, 4, 2, 2], [3, 2, 2, 2], [3, 0, 2, 2], None, None, None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [(3, 3), [0, 0, 2, 2], [0, 2, 1, 1], [1, 2, 1, 1], [2, 2, 1, 1], [2, 1, 1, 1], [2, 0, 1, 1], None, None, None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [(4, 4), [0, 0, 2, 2], [0, 2, 2, 2], [2, 1, 2, 2], [2, 0, 1, 1], [3, 0, 1, 1], [3, 3, 1, 1], [2, 3, 1, 1], None,
         None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [(4, 4), [0, 0, 3, 3], [0, 3, 1, 1], [1, 3, 1, 1], [2, 3, 1, 1], [3, 3, 1, 1], [3, 2, 1, 1], [3, 1, 1, 1],
         [3, 0, 1, 1], None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [(3, 3), [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 2, 1, 1], [1, 2, 1, 1], [2, 2, 1, 1],
         [2, 1, 1, 1], [2, 0, 1, 1], None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None],
        [(4, 4), [0, 0, 1, 1], [1, 0, 1, 1], [2, 0, 1, 1], [3, 0, 1, 1], [0, 1, 2, 2], [2, 1, 2, 2], [0, 3, 1, 1],
         [1, 3, 1, 1], [3, 3, 1, 1], [2, 3, 1, 1], None, None, None, None, None, None, None, None, None, None, None,
         None, None, None],
        [(4, 4), [0, 0, 2, 2], [2, 0, 1, 1], [3, 0, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [0, 2, 1, 2], [1, 2, 1, 2],
         [2, 2, 1, 1], [2, 3, 1, 1], [3, 3, 1, 1], [3, 2, 1, 1], None, None, None, None, None, None, None, None, None,
         None, None, None, None],
        [(4, 4), [1, 1, 2, 2], [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1], [2, 0, 1, 1], [0, 2, 1, 1], [3, 0, 1, 1],
         [0, 3, 1, 1], [1, 3, 1, 1], [2, 3, 1, 1], [3, 3, 1, 1], [3, 1, 1, 2], None, None, None, None, None, None, None,
         None, None, None, None, None],
        [(4, 4), [1, 1, 2, 2], [0, 0, 1, 1], [1, 0, 1, 1], [0, 1, 1, 1], [2, 0, 1, 1], [0, 2, 1, 1], [3, 0, 1, 1],
         [0, 3, 1, 1], [3, 1, 1, 1], [1, 3, 1, 1], [3, 2, 1, 1], [2, 3, 1, 1], [3, 3, 1, 1], None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [(4, 4), [0, 0, 1, 1], [1, 0, 1, 1], [2, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [0, 2, 1, 1],
         [1, 2, 1, 1], [2, 2, 1, 1], [3, 2, 1, 1], [0, 3, 1, 1], [1, 3, 1, 1], [2, 3, 1, 1], [3, 3, 1, 1], [3, 1, 1, 1],
         [3, 0, 1, 1], None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
         None, None, None, None, None, None, None]]

    if count <= 13 or count == 16:

        grid_width, grid_height = positions[count][0]
        width_player = int(total_width / grid_width)
        height_player = int(total_heigth / grid_height)

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

            except:
                pass



    elif count <= 25:

        grid_size = sqrt(count)
        grid_size_int = int(grid_size)
        if grid_size != grid_size_int:
            grid_size = grid_size_int + 1

        width_player = int(total_width / grid_size)
        height_player = int(total_heigth / grid_size)

        print(total_width, total_heigth, width_player, height_player)

        for i in range(count):
            row = int(i / grid_size)
            col = i % grid_size

            x = left + col * width_player
            y = top + row * height_player

            win32gui.SetWindowPos(hwnd_list[i], 0, x, y, width_player, height_player, 0)

#
# def sqrt_close(i):
#     x = sqrt(i)
#     x_int = int(x)
#     if x == x_int:
#         return x_int
#     else:
#         return x_int + 1
#
#
# def get_window_info(hwnd):
#     left1, top1, right1, bottom1 = win32gui.GetWindowRect(hwnd)
#     x, y, width, height = left1, top1, right1 - left1, bottom1 - top1
#     title = win32gui.GetWindowText(hwnd)
#     return {
#         "Title": title,
#         "Position": (x, y),
#         "Size": (width, height),
#         "hwnd": hwnd
#     }
#
#
# def windows_list():
#     with open('./json/drivers.json', 'r') as json_file:
#         player_dict1 = json.load(json_file)
#
#     def callback_windows_list(hwnd, windows):
#         if win32gui.IsWindowVisible(hwnd):
#             x = get_window_info(hwnd)
#             if x['Title'] in player_dict1.keys():
#                 windows.append(x)
#
#     windows_list = []
#     win32gui.EnumWindows(callback_windows_list, windows_list)
#
#     return windows_list
#
#
# def get_hwnds():
#     with open('./json/drivers.json', 'r') as json_file:
#         player_dict2 = json.load(json_file)
#
#     # close any duplicate players
#
#     unique = []
#     close_timer = 0
#     for w in windows_list():
#         if w['Title'] in unique:
#             print(w['hwnd'])
#             win32gui.PostMessage(w['hwnd'], win32con.WM_CLOSE, 0, 0)
#             close_timer += .1
#         else:
#             unique.append(w['Title'])
#     sleep(close_timer)
#
#     print(unique)
#     print(windows_list())
#     the_list = []
#     for player in player_dict2:
#         if player in unique:
#             for win in windows_list():
#                 if win['Title'] == player:
#                     print(player)
#                     the_list.append(win['hwnd'])
#                     break
#     return the_list
#

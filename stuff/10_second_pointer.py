# This script give the coords of the pointer for 10 seconds
#
# pip install pynput

import time
from pynput import mouse

def on_move(x, y):
    print(f"Cursor position: {x}, {y}")

def show_cursor_position():
    listener = mouse.Listener(on_move=on_move)
    listener.start()
    time.sleep(10)
    listener.stop()

if __name__ == "__main__":
    show_cursor_position()
import ctypes
import os
from pyautogui import hotkey
import time

path_image = f'{os.getcwd()}\Kazuya.jpg'

def change_wall(path_image):
    if os.path.exists(path_image):
        print("Found file wallpaper")
    else:
        print("Not found file wallpaper!!")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path_image, 0)


if __name__ == '__main__' :
    change_wall(path_image=path_image)
    hotkey("winleft", "m")

    time.sleep(5)
    wall_default = r"C:\Windows\Web\Wallpaper\Windows\img19.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_default, 0)

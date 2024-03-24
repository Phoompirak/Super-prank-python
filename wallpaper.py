import ctypes
import os
from pyautogui import hotkey
import time
# import 'Virus-prank\Kazuya.jpg'

path_image = 'Virus-prank\Kazuya.jpg'
if os.path.exists(path_image):
    print("Found file wallpaper")
else:
    print("Not found file wallpaper!!")
ctypes.windll.user32.SystemParametersInfoW(20, 0, path_image, 0)

pyautogui.hotkey("winleft", "m")

time.sleep(4)
wall_default = r"C:\Windows\Web\Wallpaper\Windows\img19.jpg"
ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_default, 0)

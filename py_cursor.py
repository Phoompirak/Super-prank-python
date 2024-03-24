import pyautogui
import keyboard
import threading
import random
import time
import os
from tkinter import messagebox

def scamer_cursor(checked):
    # the main logic to move and break
    while checked:
        # resolution of victom pc
        height = pyautogui.size().height
        width = pyautogui.size().width

        # To prevent form failsafe which breaks with cursor in corner
        pyautogui.FAILSAFE = False
        # print("Run random moveTo mouse")

        # To genrete random loc
        x = random.randint(0, width)
        y = random.randint(0, height)

        # To move cour
        pyautogui.moveTo(x, y, duration=0.2)
        # delay
        time.sleep(0.3)


def breack_move_cursor(checked):
    while checked:
        time.sleep(0.05)
        # To break the loop
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('s'):
            print("breaked")
            break
            exit()
    return


def main_cursor():
    try:
        thread = threading.Thread(target=breack_move_cursor, args=(True, ))
        thread.start()
        scamer_cursor()

    except ModuleNotFoundError as mnf:
        print(mnf)

        # ติดตั้งโมดูล pyautogui, keybord
        print("กำลังติดตั้งโมดูล pyautogui")
        os.system("pip install pyautogui")
        print("กำลังติดตั้งโมดูล keybord")
        os.system("pip install keyboard")
        time.sleep(1)
        scamer_cursor()


if __name__ == '__main__':
    # แสดงหน้าต่างข้อความแจ้งเตือนพร้อมปุ่ม "OK" และ "Cancel"
    answer = messagebox.askokcancel("Confirmation", "Do you want to exit the program?")

    if answer:
        main_cursor()
    else:
        exit("You exit with program!")

import os
import time
import keyboard
import threading
from tkinter import messagebox

def open_web(web_videos, delay):
    for web in web_videos:
        time.sleep(delay)
        os.system(f"start {web}")


web_videos = [
    # เต้น
    "https://youtu.be/dQw4w9WgXcQ?si=B13mb3k3RoRxHDeD",
    # จีน
    "https://youtu.be/ifiSa8FrK94?si=SHCdi59OUFQ82mV4",
    # อาจารย์แดง
    "https://youtu.be/Yfu6G3f8Xxc?si=ByWfAMG622osv9wd",
    # ก๋วยเตี๋ยว
    "https://youtube.com/shorts/c3V37NIQJZQ?si=dP53bTO-8VeixqaE",
    # ท่านสมาชิกชมรมคนชอบ...
    "https://youtu.be/vVZME293nEg?si=Sd41b5qePtGRZVvL"
]
delay = 3

def main_open_web(checked):
    if checked:
        open_web(web_videos, delay)

def breack_move_cursor(checked):
    while checked:
        time.sleep(0.05)
        # To break the loop
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('s'):
            print("breaked")
            os._exit(0)
            break
    return

if __name__ == '__main__':
    answer = messagebox.askokcancel("Confirmation", "Do you want to open web?")

    if answer:
        thread = threading.Thread(target=breack_move_cursor, args=(True, ))
        thread.start()
        time.sleep(10)
        main_open_web(True)
        print("Run program open web!")
    else:
        print("You exit with program!")
        os._exit(0)

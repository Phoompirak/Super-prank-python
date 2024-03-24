import os
import time
import keyboard
import threading
from py_cursor import main_cursor

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

# if __name__ == '__main__':
#     time.sleep(5)
#     thread = threading.Thread(target=main_open_web, args=(True, ))
#     thread.start()
#     main_cursor()

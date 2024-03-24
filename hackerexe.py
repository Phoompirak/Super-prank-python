from pynput.keyboard import Key, Controller
import threading
from py_cursor import scamer_cursor
import time
import random

# จำลองคีบอร์ดแบบ third Party(ตัวกลาง)
keyboard = Controller()
color_list = ["a", "c", "d"] # เขียว, แดง, ม่วง
word_dynamic = [
    "ผีหลอกกกกกกกก แฮร่(≧◇≦)"
    "คุณโดนแฮ็กสำเร็จ",
    "กำลังรันออโต้บอท",
    "ทำการรีโมทเข้าเข้าเครื่องคอม",
    "ทำการดูดข้อมูลทั้งหมดสำเร็จ",
    "ทำการดูดข้อมูลทั้งหมดสำเร็จ",
    "คามุย!"
]

# เอาไว้ delay กันโค้ดทำงานเร็วจนเครื่องค้าง
def random_time(): # 0.1-1 แบบมีทศนิยม 2 ตำแหน่ง
    return float(f"{random.uniform(0.1, 1):.2f}")

def open_cmd():
    # เปิด Run system
    keyboard.press(Key.cmd) # Key.cmd = winodws button
    keyboard.press('r') # press = กดค้าง
    keyboard.release('r') # release = เลิกกดค้าง
    keyboard.release(Key.cmd)
    time.sleep(0.1)

    # เปิด Command Prompt
    keyboard.type("cmd")
    time.sleep(0.1)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)



def check_file_all(color):
    time.sleep(random_time())

    keyboard.type(f"color {color}")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    
    keyboard.type("dir /s")
    time.sleep(random_time())

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random_time())


def open_notepad():
    # เปิด Run system
    keyboard.press(Key.cmd) # Key.cmd = winodws button
    keyboard.press('r') # press = กดค้าง
    keyboard.release('r') # release = เลิกกดค้าง
    keyboard.release(Key.cmd)
    time.sleep(random_time())

    # เปิด notepad
    keyboard.type("notepad")
    time.sleep(random_time())

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random_time())

    # tab ใหม่
    keyboard.press(Key.ctrl)
    keyboard.press('n')
    keyboard.release('n')
    keyboard.release(Key.ctrl)
    time.sleep(random_time())



def writting_notepad(word_dynamic):
    for i in range(30):
        keyboard.type("YOU JUST GOT HACKED!!!")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.07)

    keyboard.release(Key.enter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(random_time())

    for word in word_dynamic:
        keyboard.type(word)
        time.sleep(random_time())

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(random_time())

def main_hackerexe(checked):
    for color in color_list:
        open_cmd()
        check_file_all(color)
        time.sleep(random_time())
    
    open_cmd()
    time.sleep(random_time())
    keyboard.type("netsh wlan show profile")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    print("Open notepad")

    time.sleep(3)
    open_notepad()

    time.sleep(3)
    writting_notepad(word_dynamic)

# if __name__ == '__main__':
#     thread = threading.Thread(target=scamer_cursor, args=(True, ))
#     thread.start()
#     print("Started main_hackerexe")
#     main_hackerexe(True)

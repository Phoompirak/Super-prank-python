import os
import time
import keyboard
import multiprocessing
from threading import Thread
from tkinter import messagebox
from multiprocessing import Process

from virus_bomb import main_virus
from prank_sound import sound_prank
from Open_web import main_open_web
from hackerexe import main_hackerexe
from py_cursor import scamer_cursor

def cancel_prank(checked):
    def handler():
        print("Received Ctrl+s signal, exiting...")
        all_working_process = multiprocessing.active_children()
        if len(all_working_process) > 0:
            for work in all_working_process:
                print(f"Cancel: {work}")
                work.terminate()
                work.join()
        print("All pranks canceled.")
        os._exit(0)

    keyboard.add_hotkey('ctrl+s', handler)

    while checked:
        try:
            keyboard.wait()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(0.5)

def main_all_prank():
    pranks = [scamer_cursor, main_open_web, sound_prank, main_virus, main_hackerexe]
    for prank in pranks:
        time.sleep(2)
        prank_thread = Process(target=prank, args=(True, ))
        prank_thread.start()
        print(f"----------------\nStarted process for {prank.__name__}\n--------------")

if __name__ == '__main__':
    # แสดงหน้าต่างข้อความแจ้งเตือนพร้อมปุ่ม "OK" และ "Cancel"
    answer = messagebox.askokcancel("Confirmation", "Do you want to exit the program?")

    exit_prank = Thread(target=cancel_prank, args=(True, ))
    print("Start thread exit program")
    exit_prank.start()

    if answer:
        time.sleep(1)
        main_all_prank()
    else:
        print("You exit with program!")
        os._exit(0)
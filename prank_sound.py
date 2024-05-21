try:
    import winsound
    import time
    import random
    from tkinter import messagebox
    import threading
    import keyboard
    import os
except Exception as err:
    print("Error sound prank:", err)

def sound_prank(checked):
    # กำหนดค่าความถี่และระยะเวลาของเสียง Beep
    duration = 1000   # ระยะเวลา (มิลลิวินาที)
    if checked:
        for i in range(10):
            time.sleep(0.5)
            # เล่นเสียง Beep
            frequency = random.randint(500, 2000)  # ความถี่ (Hz)
            print(f'Frequency: {frequency}')
            winsound.Beep(frequency, duration)

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
    answer = messagebox.askokcancel("Confirmation", "Do you want to prank sound?")

    if answer:
        thread = threading.Thread(target=breack_move_cursor, args=(True, ))
        thread.start()
        time.sleep(10)
        sound_prank(True)
        print("Run program sound prank")
    else:
        print("You exit with program!")
        os._exit(0)
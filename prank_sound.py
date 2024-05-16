try:
    import winsound
    import time
    import random
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

if __name__ == '__main__':
    sound_prank(True)
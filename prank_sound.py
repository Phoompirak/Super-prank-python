import winsound
import time

def sound_prank(checked):
    # กำหนดค่าความถี่และระยะเวลาของเสียง Beep
    frequency = 1000  # ความถี่ (Hz)
    duration = 1000   # ระยะเวลา (มิลลิวินาที)
    if checked:
        for i in range(10):
            time.sleep(0.5)
            # เล่นเสียง Beep
            winsound.Beep(frequency, duration)

if __name__ == '__main__':
    sound_prank()
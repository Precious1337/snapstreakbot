import time
import pyautogui


click_positions = [(994, 493), (996, 792), (1144, 833), (907, 455), (1004, 825)]
timer_duration = 3


while True:
    for position in click_positions:
        start_time = time.time()
        while (time.time() - start_time) < timer_duration:
            time_left = timer_duration - (time.time() - start_time)
            print(f"Time left: {time_left:.2f} seconds", end='\r')
            time.sleep(1)
        pyautogui.click(position[0], position[1])
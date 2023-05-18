import pyautogui
import time

print("Waiting for 5 seconds...")
time.sleep(5)
print("Click on the screen...")
click_x, click_y = pyautogui.position()
print(f"Clicked at position ({click_x}, {click_y})")
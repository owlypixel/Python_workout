import pyautogui, time

print(pyautogui.size())
pyautogui.click(23, 1060, duration=2)
pyautogui.typewrite("paint.net", interval=0.3)
pyautogui.click(78, 566, duration=2)
time.sleep(5)
# pyautogui.hotkey('ctrl', 'n')
coords = pyautogui.locateCenterOnScreen('edge.png')
pyautogui.click(coords)


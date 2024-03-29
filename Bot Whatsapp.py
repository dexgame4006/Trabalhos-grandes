import pyautogui
import time 

x=input('Mandar mensagem a:')
y=input('Mensagem:')

pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('w')
pyautogui.press('enter') 

time.sleep(2.5)
pyautogui.write(x)
time.sleep(1)
pyautogui.click(x=116, y=193)

time.sleep(1)
pyautogui.write(y)
pyautogui.press('enter')
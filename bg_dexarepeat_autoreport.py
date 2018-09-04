import os
import pyautogui

os.startfile('C:\Program Files (x86)\Sanford Health\One Chart - LTSR\One Chart')
pyautogui.FAILSAFE = True

# 120 second delay to let program open up
pyautogui.PAUSE = 120

# arbitray delay to let program open up
pyautogui.moveTo(100, 200)

# reset delay to 2 seconds
pyautogui.PAUSE = 2

# username and password and resource clicks.  Opens up program.
pyautogui.click(824, 516)
pyautogui.typewrite('clahn')
pyautogui.click(824, 562)
# pyautogui.press('\t')
pyautogui.typewrite('xwp')
# switched to AutoHotkey, no longer need backspace.  Space triggers snippet.
pyautogui.press('space')
# pyautogui.press('backspace')
# pyautogui.press('enter')
pyautogui.click(958, 602)
pyautogui.PAUSE = 15
pyautogui.click(874, 549)
pyautogui.PAUSE = 10


# open myreports and click BGY DEXA Repeat Report.
pyautogui.click(124, 33)
# Wait 5 minutes for report to generate before trying to export.
pyautogui.PAUSE = 300
# Change this click location for other reports.
pyautogui.click(1220, 191)

'''
If key presses worked for EIPC this would open export menu
pyautogui.keyDown('alt')
pyautogui.press('o')
pyautogui.keyUp('alt')
'''

# Opens export tab and clicks export to file
pyautogui.PAUSE = 2
pyautogui.click(205, 108)
pyautogui.click(280, 226)
# Pause to let big reports load here.
pyautogui.PAUSE = 300
# Click load all dialogue box to load big reports
pyautogui.click(1023, 571)


pyautogui.PAUSE = 3
# types file name and saves to INBOX
pyautogui.doubleClick(282, 384)
pyautogui.press('del')
# Rename report in Phrase Express
pyautogui.typewrite('xxbgdx')
# switched to AutoHotkey, no longer need backspace.  Space triggers snippet.
pyautogui.press('space')
# pyautogui.press('backspace')
pyautogui.PAUSE = 30
pyautogui.click(515, 382)

# closes EPIC
pyautogui.click(1901, 8)
pyautogui.click(1016, 563)

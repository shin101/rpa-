import pyautogui

pyautogui.sleep(5)
# pyautogui.write("12345", interval=1) 
# interval means takes 1 sec to write every letter
# pyautogui.write is not compatible with non-English and letters.
# to enable writing in other languages, we will cover that later
# pyautogui.write([])

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"], interval=0.25)
# t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 2번,l a 순서대로 적고 enter

# 특수 문자 such as $
# pyautogui.keyDown("shift")
# pyautogui.press("4") # press는 눌렀다 때는 동작
# pyautogui.keyUp("shift")

# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a") # same as press("a")
# pyautogui.keyUp("ctrl") # Ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl","a") # this does above 4 lines of code into one

# #To allow korean you need to pip install pyperclip

import pyperclip
# pyperclip.copy("한국어") #"한국어" 글자를 클립보드에 저장
# pyautogui.hotkey("ctrl","v")

# # alternatively you can also create a function

# def my_write(text):
#     pyautogui.copy(text)
#     pyautogui.hotkey("ctrl","v")

# my_write("안녕")

# mac : cmd + shift + option + q 자동화 프로그램 종료
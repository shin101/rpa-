import pyautogui
# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

pyautogui.mouseInfo()

pixel = pyautogui.pixel(28, 18)
print(pixel) # shows RGB value

print(pyautogui.pixelMatchesColor(28, 18, (34,167,242))) # last 3 is RGB value
#return True or False


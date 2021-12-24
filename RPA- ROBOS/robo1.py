import pyautogui as p

p.hotkey('win', 'r')
p.sleep(1)
p.typewrite('notepad')
p.sleep(3)
p.press('enter')
p.sleep(3)
p.typewrite('AMOR VOCE E A MULHER MAIS LINDA DO MUNDO ')
valor = p.getActiveWindow()
#valor.close()
#p.press('right')
#p.sleep(1)
#p.press('enter')
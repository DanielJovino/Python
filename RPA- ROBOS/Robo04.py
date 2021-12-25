import pyautogui as p

p.sleep(2)
p.moveTo(x=45, y=38, duration=2)
p.doubleClick(x=45, y=38)
p.sleep(4)
p.write('www.udemy.com')
p.press('enter')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(4)

localPesq = p.locateOnScreen('Pesquisa.PNG', confidence=0.8)
localPesquisa = p.center(localPesq)
xPesquisa, yPesquisa = localPesquisa
p.moveTo(xPesquisa, yPesquisa, duration=1)
p.click(xPesquisa, yPesquisa)
p.sleep(1)
p.write('Daniel')


#p.sleep(2)
#print(p.position())

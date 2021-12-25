import rpa as r
import pyautogui as p

r.init()
r.url('https://www.melhorcambio.com/dolar-hoje')
janela = p.getActiveWindow()
janela.maximize()
p.sleep(3)
dolar = r.read('//*[@id="comercial"]')
r.close()

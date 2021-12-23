import rpa as r 
import pyautogui as p

r.init()
r.url('https://www.google.com/')
janela = p.getActiveWindow()
janela.maximize()
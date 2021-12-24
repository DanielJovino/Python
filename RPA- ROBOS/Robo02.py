"""
Pesquisar no google
"""
import rpa as r
import pyautogui as p

r.init()
r.url('https://google.com.br')
janela = p.getActiveWindow()
janela.maximize()
r.wait(2.0)
r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input', 'RPA[enter]')
r.snap('page','rpa_page.png')
r.wait(2.0)
r.close()

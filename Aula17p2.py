""""
Funcoes (def) em python - return - Aula 16 (Parte 2)
"""

def divisao(n1, n2):
    if n2 > 0:
        return  n1 / n2

divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('Conta invalida')
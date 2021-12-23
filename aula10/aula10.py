"""
== igual
>= maior qu ou igual a
< menor
<= menor que ou igual a
!= diferente
"""

nome =  input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? ') )

# Limite para pegar empréstimo
#idade_limite = 18

idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o imprestimo')
else:
    print(f'{nome} não pode pegar o emprestimo')

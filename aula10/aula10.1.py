"""
Operadores Lógicos
and, or , not
in e not in

not = inversão
"""
# (Verdadeiro E False) = Falso
#comparacao1 and comparacao

# Verdadeiro ou Verdadeiro
#comp1 or comp2

#nome = 'Daniel'

#if 'z' not in nome:
   # print("Existe.")
#else :
    #print("Não existe")

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Daniel'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuário senha incorretos')
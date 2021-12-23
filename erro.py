#Erro em tempo de compilação
#Erros em tempo de execução
#Erros de logica

def divisao(a, b):
    try:
        print(a/b)
    except Exception as e:
        print('DIvisão inválida')
        print(e)

divisao(20, 0)
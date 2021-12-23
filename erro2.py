#Erro em tempo de compilação
#Erros em tempo de execução
#Erros de logica

try:
    a = float(input('Digite o numero A:')) #ValueError
    b = float(input('Digite o numero B : '))

    print(a/b) #ZeroDivisionError
except ValueError as error:
    print('Input invalido digite apenas numeros ')
except ZeroDivisionError as error:
    print('Não pode ser feita a divisão por zero')
except Exception as error:
    print('Algum erro ocorreu')
finally:
    print('Fim do programa')
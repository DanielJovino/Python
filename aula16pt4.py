

Variavel = 'valor'

def func():
    print(Variavel)

def func2():

    Variavel = 'Outro valor'
    print(Variavel)

func()
func2()

print(Variavel)

#isso nao e uma boa pratica 
#use o return
AGENDA = {}

AGENDA ['Matheus'] = {
    'Telefone' : '99999999',
    'email' : 'guilherme@solyd.com.br',
    'endereco': 'Av.1',

}

AGENDA ['Fernando'] = {
    'Telefone' : '99999999',
    'email' : 'Fernando@solyd.com.br',
    'endereco': 'Av.1',
}

def mostrar_contatos():
   if AGENDA:
       for contato in AGENDA:
            buscar_contato(contato)
            print('--------------------------')
   else:
       print('>>>>>>Agenda vazia')

def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print("Telefone:", AGENDA[contato]['Telefone'])
        print("endereço:", AGENDA[contato]['endereco'])
        print("email:", AGENDA[contato]['email'])
        print('-------------------------------------------')
    except KeyError:
        print('Contato inexistente')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)


def incluir_editar_contato(contato):
    telefone = input('Digite o telefone: ')
    email = input('Digite o nome o email: ')
    endereco = input('Digite o nome o endereco: ')

    AGENDA[contato] =  {
        'Telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print('>>>>>>Contato {} adicionado/editado com sucesso'.format(contato))

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print()
        print('>>>>>>Contato {} excluido com sucesso'.format(contato))
        print()
    except KeyError:
        print('Contato inexistente')
    except Exception as error:
        print('>>>>> Um erro inesperado ocorreu')
        print(error)


def imprimir_menu():
    print('-------------------------------------------')
    print('1- Mostrar todos os contatos da Agenda')
    print('2- Buscar contato')
    print('3- Incluir contato')
    print('4- Editar contato')
    print('5- Excluir contato ')
    print('0- Sair do Menu')
    print('-------------------------------------------')

while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    if opcao == '2':
        contato = input('Digite o nome do contato:')
        buscar_contato(contato)
    if opcao == '3':
        contato = input('Digite o nome do contato: ')
        try:
            AGENDA[contato]
            print('>>>> Contato já existe ')
        except KeyError:
            incluir_editar_contato(contato)
    elif opcao == '4':
        contato = input('Difite o nome do contato:')
        try:
            AGENDA[contato]
            print('>>>> Editando contato: ', contato)
            incluir_editar_contato(contato)
        except KeyError:
            print('contato não existe')

    if opcao == '5' :
        contato = input('Digite o nome do Contatoo: ')
        excluir_contato(contato)
    if opcao == '0':
        print('Fechando programa ')
        break
    else:
        print('>>>>>>Opção invalida')


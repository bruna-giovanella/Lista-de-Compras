from funcs import add
from funcs import remove
from funcs import show
from funcs import sys_exit



validador = True
lista = []
quantia = []

print('\n=====================================')
print('   Bem-vindo à sua LISTA DE COMPRAS :)')
print('=====================================\n')

while validador:

    # MENU
    def menu():
        print('==================== MENU ====================')
        print('1. Adicionar item')
        print('2. Remover item')
        print('3. Exibir lista')
        print('4. Sair')
        print('==============================================')

        global action
        action = input('\nQual ação deseja realizar?\nAção desejada: ')

        if action.isdigit():
            action = int(action)

            if action not in [1, 2, 3, 4]:
                print('\nATENÇÃO!\nO valor informado é inválido. Por favor, informe um novo valor.\n')
                menu()

        elif not action.isdigit():
            print('\nATENÇÃO!\nO valor informado é inválido. Por favor, informe um novo valor.\n')
            menu()

        else:
            return action

    menu()

#############################################################


    # CAMINHO
    if action == 1:
        add(lista, quantia)
    elif action == 2:
        remove(lista, quantia)
    elif action == 3:
        show(lista, quantia)
    elif action == 4:
        sys_exit()

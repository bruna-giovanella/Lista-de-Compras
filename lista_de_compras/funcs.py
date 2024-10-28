
# AÇÕES



# adicionar
def add(lista, quantia):
    print('\n================================================')
    print('               ADICIONAR ITEM                   ')
    print('================================================')

    validador_add = True
    while validador_add == True:
        produto = input('Informe o produto que deseja adicionar\nProduto: ').strip().capitalize()

        if produto in lista:
            confirmar_adicao = input('\nO produto já está na lista.\nDeseja adicioná-lo mesmo assim? (s/n): ').lower()
            indice = lista.index(produto)

            if confirmar_adicao == 's':
                quantia[indice] += 1
                print(f'\nO item "{produto}" foi adicionado com sucesso!\n') 
            else:
                print('\nO item não foi adicionado.\n')

        else:
            quantia_produto = input('\nQuantos produtos você deseja adicionar?\nQuantidade: ')

            if not quantia_produto.isdigit():
                print('\nATENÇÃO!\nO valor informado é inválido.\n')
            else:
                lista.append(produto)
                quantia_produto = int(quantia_produto)
                quantia.append(quantia_produto) 
                print(f'\nO item "{produto}" foi adicionado com sucesso!\n')

        adicionar_novo = input('Deseja adicionar um novo valor? (s/n)').lower()
        if adicionar_novo=='s':
            validador_add = True
        else:
            validador_add = False

        print('================================================\n')






#############################################################






# remover
def remove(lista,quantia):
    print('\n================================================')
    print('               REMOVER ITEM                    ')
    print('================================================')

    validador_remove = True
    while validador_remove == True:
        remover = input('Informe o produto que deseja remover\nProduto: ').strip().capitalize()
        

        if remover in lista:
            indice = lista.index(remover)

            if quantia[indice] > 1:
                print(f'Você possui {quantia[indice]} itens em sua lista.')
            else:
                print(f'Você possui {quantia[indice]} item em sua lista.')
            quantidade_remover = int(input('\nQuantos produtos você deseja remover?\nQuantidade: '))

            if quantidade_remover == quantia[indice]:
                lista.remove(remover)
                print(f'\nO item "{remover}" foi removido com sucesso!\n')
            elif quantidade_remover > quantia[indice]:
                print('O valor informado é maior que a quantia na lista')
                
            else:
                quantia[indice] -= quantidade_remover
        else:
            print(f'O item "{remover}" não está na lista.')

        remover_novo = input('Deseja remover um novo valor? (s/n)').lower()
        if remover_novo=='s':
            validador_remove = True
        else:
            validador_remove = False

        print('================================================\n')






#############################################################






# exibir

def show(lista, quantia):
    print('\n================================================')
    print('                  LISTA DE COMPRAS              ')
    print('================================================')

    if lista:
        for indice, produto in enumerate(lista):
            print(f'{indice+1}. {produto} ({quantia[indice]})')

        print('\n')
    else:
        print('A lista está vazia :(\n')

    print('================================================\n')








#############################################################






# sair
def sys_exit():
    print('Saindo...')
    exit()
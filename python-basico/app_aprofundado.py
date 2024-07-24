import os #importar a funcao de limpar a tela da biblioteca

# restaurantes = [] -> isso é uma lista
# restaurantes = () -> isso é uma tupla (diferente da lista, os valores internos nao podem ser alterados e devem sempre ser definidas)
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiana', 'ativo':False}]  # somente os que estao dentro {} é um dicionario, o [{}] é estrutura de dados que tem uma lista e dentro um conjunto de dicionarios dentro dele usando chave:valor

def exibir_nome_do_programa():
    print ('=================================')
    print('Sabor Express')
    print ('=================================')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def escolher_opcao():

    # Para tirar os erros de excecao por letras, iremos inserir o try...except!

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # print(f'Você escolheu a opção: {opcao_escolhida}!') #interpolação de variaveis e strings f-string

        # se aparecer 50 opcoes, teriamos que criar 50 linhas de opcoes, vamos simplicar isso usando funcoes... tirar o "print('Encerrando o programa')"

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

# print(type(opcao_escolhida)) tipo string
# print(type(1)) tipo int
# a funcao input retorna uma string e o 1 é um inteiro...por isso que a comparação abaixo não funciona, temos das formas de resolver:

# opcao_escolhida = int(opcao_escolhida) ou
# opcao_escolhida = int(input('Escolha uma opção: '))

def finalizar_app():
    os.system('cls') #limpar a tela
    print('Finalizando o app')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
     '''Essa função é responsável por cadastrar um novo restaurante
     
        Inputs:
        - Nome do restaurante
        - Categoria

        Outputs:
        - Adiciona um novo restaurante a lista de restaurantes
     
     ''' #docstring = documentar suas funções com o resumo oq ela faz
     os.system('cls')
     print('Cadastro de novos restaurantes\n')
     nome_do_restaurante = input('Digite o nome do restaurante: ')
     categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
     dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} #criando um novo dic
     restaurantes.append(dados_do_restaurante) #inserindo um novo dic dentro da lista
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
     voltar_ao_menu_principal()

def listar_restaurante():
     os.system('cls')
     print('Exibindo os restaurantes\n')
     print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
     for i in restaurantes:
        nome_restaurante = i['nome']
        categoria = i['categoria']
        ativo = 'ativado' if i['ativo'] else 'desativado' # operacao ternaria
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') # a funcao ljust coloca espaçamento entre palavras
     print('\n')
     voltar_ao_menu_principal() 

def alternar_estado_restaurante():
    os.system('cls')
    print('Alternando estado do restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante que você deseja alterar o estado: ')
    
    restaurante_encontrado = False #variavel de contenção = rastrear condições específicas, como encontrar um item em uma lista, verificar se um valor atende a um critério específico, entre outros casos onde é necessário saber se um evento ocorreu ou não durante a execução de um código.
    
    for i in restaurantes:
        if nome_do_restaurante == i['nome']:
            restaurante_encontrado = True # contém o estado de controle durante a execução do loop for.
            i['ativo'] = not i['ativo'] # o not ele alterna o estado do booleano
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if i['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso' # Operação ternária!
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

# para falar que esse sera o arq principal e nao podera ser importado por outros arq python

def main():
    exibir_nome_do_programa()    
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
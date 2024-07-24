import os #importar a funcao de limpar a tela da biblioteca

restaurantes = []

def exibir_nome_do_programa():
    print ('=================================')
    print('Sabor Express')
    print ('=================================')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
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
            print('Ativar restaurante')
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
     os.system('cls')
     print('Cadastro de novos restaurantes\n')
     nome_do_restaurante = input('Digite o nome do restaurante: ')
     restaurantes.append(nome_do_restaurante)
     print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
     voltar_ao_menu_principal()

def listar_restaurante():
     os.system('cls')
     print('Exibindo os restaurantes\n')
     for i in restaurantes:
        print('- ' + i)
     voltar_ao_menu_principal() 

# para falar que esse sera o arq principal e nao podera ser importado por outros arq python

def main():
    exibir_nome_do_programa()    
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
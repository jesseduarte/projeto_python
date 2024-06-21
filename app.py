print ('=================================')
print('Sabor Express')
print ('=================================')
print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))

# print(f'Você escolheu a opção: {opcao_escolhida}!') #interpolação de variaveis e strings f-string

print(type(opcao_escolhida)) #tipo string
print(type(1)) #tipo int
# a funcao input retorna uma string e o 1 é um inteiro...por isso que a comparação abaixo não funciona, temos das formas de resolver:

# opcao_escolhida = int(opcao_escolhida) ou
# opcao_escolhida = int(input('Escolha uma opção: '))


if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa')
print('\nPython na Escola de Programação da alura.\n')

nome = 'Jessé'
idade = 32

# f-string
print(f'Meu nome é {nome} e tenho {idade} anos\n')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))

pi_arredondado = 3.14159

# f-string
print(f'o valor arredondado de pi é: {pi_arredondado:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi_arredondado))

# Utilizando a função round() e f-string
print(f'O valor arredondado de pi é: {round(pi_arredondado, 2)}')

# Para imprimir a palavra ‘ALURA’ com cada letra em cada linha com a função print utilizando o parâmetro sep para especificar o separador entre os argumentos
print('A','L','U','R','A',sep='\n')

# Colocar descricoes de produtos de um site...são descrições longas, logo use as aspas triplas ''' ou o sep como exemplo acima
print ('''Camiseta Unissex
Tamanho: P, M, G, GG
Material: 100% algodao
Cores disponiveis: Preto, Branco, Vermelho\n''')

# coletar as informações e imprimir a mensagem desejada, seguindo o formato: "O departamento de [Departamento] é liderado por [Responsável].

print('====================')
print('Organo - plataforma de organogramas para empresas\n')
Departamento = input('Digite seu departamento: ')
Responsavel = input('Digite seu responsável: ')
print(f'O departamento de {Departamento} é liderado por {Responsavel}.')



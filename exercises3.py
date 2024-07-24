def configurar_tempo_foco(tempo_foco):
    if tempo_foco >= 25 and tempo_foco <= 45:
        return 'tempo de foco aceitável'
    else:
        return 'tempo de foco inaceitável'
    
def categoria_idade(idade):
    if 0 <= idade >= 12:
        return 'Criança'
    elif 13 <= idade >= 18:
        return 'Adolescente'
    else:
        return 'Adulto'

nome_usuario = 'jesse'
senha = '123'
    
def autenticacao(nome_usuario, senha):
    if  nome_usuario == nome_usuario_input and senha == senha_input:
        return 'Logado!'
    else:
        return 'usuario e/ou senha inválidos'
    
tempo_foco = int(input('Quanto tempo você deseja para o período de foco: '))
print(configurar_tempo_foco(tempo_foco))

idade = int(input('Qual sua idade: '))
print(categoria_idade(idade))

nome_usuario_input = input('Entre com o seu usuário: ')
senha_input = input('Entre com a sua senha: ')
print(autenticacao(nome_usuario, senha))
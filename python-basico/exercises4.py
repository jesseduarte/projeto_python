'''
Imagine que você está trabalhando na Techsafe, uma empresa especializada em segurança tecnológica. Sua liderança pediu para você 
revisar um trecho de código em Python que utiliza dicionários para armazenar dados sensíveis dos clientes. O objetivo é garantir que 
o uso de dicionários e operadores ternários esteja correto para otimizar a performance e a legibilidade do código. Dada a seguinte 
estrutura de dicionário:
'''
credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

'''
Você deseja verificar o status de um usuário chamado 'bob456' e, caso esteja inativo, enviar um alerta. Qual seria o código correto 
para realizar essa ação utilizando um operador ternário?
'''
alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] else 'Sem alerta'
#OU alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] == 'inactive' else 'Sem alerta'
print (alerta)
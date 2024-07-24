'''Imagine que você está desenvolvendo um projeto para um serviço de streaming de música. Sua tarefa é melhorar o algoritmo de 
recomendação de músicas, garantindo que os usuários recebam sugestões mais precisas com base em seus gêneros favoritos.

No processo de desenvolvimento, você escreveu a seguinte função para classificar uma música como 'recomendada', 'neutra' ou 'não 
recomendada' com base na preferência do gênero musical do usuário'''

def classificar_musica (genero_favorito, genero_musica):
    if genero_favorito == genero_musica:
        return 'recomendada'
    elif genero_favorito == 'pop' or genero_favorito == 'Rock':
        return 'neutra'
    else:
        return 'não recomendada'
    
resultado = classificar_musica('rock','rock')
print(f'A musica será {resultado}')
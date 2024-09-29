'''Dados as orientações até então, faça as seguintes instruções: a. Crie uma lista chamada animais que contenha os elementos 'cachorro', 'gato', 'papagaio', e 'tartaruga'; b. Imprima o primeiro e o último elemento da lista animais; c. Modifique o segundo elemento da lista animais para 'coelho'.'''

# a. Cria uma lista chamada "animais" com os elementos especificados: 'cachorro', 'gato', 'papagaio' e 'tartaruga'
animais = ['cachorro', 'gato', 'papagaio', 'tartaruga']

# b. Imprime o primeiro elemento da lista (índice 0) e o último elemento (índice -1)
print(animais[0])  # Imprime 'cachorro', que é o primeiro elemento
print(animais[-1]) # Imprime 'tartaruga', que é o último elemento

# c. Modifica o segundo elemento da lista (índice 1) de 'gato' para 'coelho'
animais[1] = 'coelho'

# Exibe a lista atualizada, agora com 'coelho' no lugar de 'gato'
print(animais)

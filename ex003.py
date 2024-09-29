'''Crie uma lista chamada temperaturas com os valores [30, 22, 25, 28, 31, 27, 29]. Aumente todas as temperaturas menores que 25 em 5 graus.'''

# Cria uma lista chamada "temperaturas" com os valores fornecidos
temperaturas = [30, 22, 25, 28, 31, 27, 29]

# Percorre a lista de temperaturas usando o índice de cada elemento
for i in range(len(temperaturas)):  # "range(len(temperaturas))" gera uma sequência de índices de 0 até o tamanho da lista
    # Verifica se a temperatura atual (na posição i) é menor que 25
    if temperaturas[i] < 25:
        # Se a condição for verdadeira, aumenta o valor da temperatura em 5 graus
        temperaturas[i] += 5

# Exibe a lista de temperaturas atualizada, já com o ajuste feito
print(temperaturas)

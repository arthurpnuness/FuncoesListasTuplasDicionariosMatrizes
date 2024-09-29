'''Peça ao usuário para digitar duas sequências de 5 números e armazene em duas listas distintas. Após, faça um programa que junte essas duas listas em uma só.'''


# Inicializa o contador com o valor 0
contador = 0

# Cria uma lista vazia chamada "lista1" para armazenar os números da primeira sequência
lista1 = []  # Lista para armazenar a primeira sequência de números
# Cria uma lista vazia chamada "lista2" para armazenar os números da segunda sequência
lista2 = []  # Lista para armazenar a segunda sequência de números

# Coleta 5 números para a primeira lista usando um loop "while"
while contador < 5:
    # Solicita ao usuário que digite um número inteiro para a primeira lista
    num1 = int(input('Digite um número para a primeira lista: '))
    # Adiciona o número digitado à lista1
    lista1.append(num1)
    # Incrementa o valor do contador para controlar o número de iterações
    contador += 1

# Redefine o contador para 0 para reutilizá-lo na segunda sequência de números
contador = 0  # Resetar o contador para usar na segunda sequência

# Coleta 5 números para a segunda lista usando um loop "while"
while contador < 5:
    # Solicita ao usuário que digite um número inteiro para a segunda lista
    num2 = int(input('Digite um número para a segunda lista: '))
    # Adiciona o número digitado à lista2
    lista2.append(num2)
    # Incrementa o contador após cada número adicionado à lista
    contador += 1

# Concatena as duas listas "lista1" e "lista2" usando o operador de soma "+"
concatenacao = lista1 + lista2

# Exibe a lista concatenada
print('Lista concatenada:', concatenacao)


    
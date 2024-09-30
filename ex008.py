'''Peça ao usuário para digitar uma sequência de 10 números. Em seguida, crie duas listas a partir desta sequência: uma contendo os números pares e outra contendo os números ímpares.'''

# Inicializa uma lista vazia para armazenar os números inseridos pelo usuário
lista = []

# Inicializa um contador para garantir que 10 números serão solicitados ao usuário
contador = 0

# Inicializa uma lista para armazenar os números pares
pares = []

# Inicializa uma lista para armazenar os números ímpares
impares = []

# Enquanto o contador for menor que 10, o laço continua
while contador < 10:
    # Pede ao usuário para inserir um número e converte a entrada para inteiro
    numbers = int(input('Digite um numero: '))
    
    # Adiciona o número inserido à lista principal
    lista.append(numbers)
    
    # Incrementa o contador para controlar o número de entradas
    contador += 1

# Percorre a lista de números inseridos pelo usuário
for i in lista:
    # Se o número for divisível por 2, é par e é adicionado à lista 'pares'
    if i % 2 == 0:
        pares.append(i)
    # Caso contrário, o número é ímpar e é adicionado à lista 'impares'
    else:
        impares.append(i)

# Exibe a lista de números pares
print('Numeros pares: ', pares)

# Exibe a lista de números ímpares
print('Numeros impares: ', impares)

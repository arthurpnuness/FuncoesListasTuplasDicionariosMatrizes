'''Peça ao usuário para digitar duas sequências de 5 números e armazene-as em duas listas distintas. Em seguida, faça um programa que procure os elementos comuns entre elas e os junte em uma terceira lista.'''

# Inicializa o contador com o valor 0
contador = 0

# Cria uma lista vazia chamada "lista1" para armazenar os números da primeira lista
lista1 = []

# Cria uma lista vazia chamada "lista2" para armazenar os números da segunda lista
lista2 = []

# Preenchendo a primeira lista com 5 números fornecidos pelo usuário
while contador < 5:
    # Solicita que o usuário digite um número para a 1ª lista
    num1 = int(input('Digite um numero para a 1ª Lista: '))
    # Adiciona o número digitado à lista1
    lista1.append(num1)
    # Incrementa o contador para garantir que o loop seja executado 5 vezes
    contador += 1

# Redefine o contador para 0 para reutilizá-lo no preenchimento da segunda lista
contador = 0

# Preenchendo a segunda lista com 5 números fornecidos pelo usuário
while contador < 5:
    # Solicita que o usuário digite um número para a 2ª lista
    num2 = int(input('Digite um numero para a 2ª Lista: '))
    # Adiciona o número digitado à lista2
    lista2.append(num2)
    # Incrementa o contador para garantir que o loop seja executado 5 vezes
    contador += 1

# Cria uma lista vazia chamada "comuns" para armazenar os elementos comuns entre as duas listas
comuns = []

# Percorre cada número da lista1
for i in lista1:
    # Verifica se o número atual da lista1 também está presente na lista2
    if i in lista2:
        # Se o número estiver presente em ambas as listas, ele é adicionado à lista "comuns"
        comuns.append(i)

# Exibe a lista "comuns" contendo os elementos que aparecem em ambas as listas
print(comuns)


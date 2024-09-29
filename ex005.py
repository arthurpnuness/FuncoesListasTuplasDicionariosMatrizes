'''Peça ao usuário para digitar uma sequência de 10 números. Após, procure o maior e o menor número e apresente na tela.'''

# Inicializa a variável "contador" com o valor 0 para controlar o número de iterações
contador = 0

# Cria uma lista vazia chamada "numeros" para armazenar os números digitados pelo usuário
numeros = []  # Lista para armazenar os números

# Inicia um loop "while" que continuará até que o contador alcance 10 (pedir 10 números)
while contador < 10:  # O loop continuará enquanto o contador for menor que 10
    # Solicita ao usuário que digite um número inteiro
    num = int(input('Digite um numero: '))
    # Adiciona o número digitado à lista "numeros" usando o método "append"
    numeros.append(num)
    # Incrementa o valor do contador em 1 a cada iteração
    contador += 1

# Após o loop, usa a função "max" para encontrar o maior número na lista "numeros"
maior = max(numeros)
# Usa a função "min" para encontrar o menor número na lista "numeros"
menor = min(numeros)

# Exibe o maior e o menor número encontrados na lista
print(f'O maior numero da lista é {maior} e o menor da lista é {menor}')



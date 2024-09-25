'''Peça ao usuário para digitar uma sequência de 10 números. Após, procure o maior e o menor número e apresente na tela.'''

contador = 0
numeros = []  # Lista para armazenar os números

while contador < 10:  # Alterado para contar até 10 números
    num = int(input('Digite um numero: '))
    numeros.append(num)  # Adiciona cada número à lista
    contador += 1

# Usa max e min para encontrar o maior e o menor número na lista
maior = max(numeros)
menor = min(numeros)

print(f'O maior numero da lista é {maior} e o menor da lista é {menor}')


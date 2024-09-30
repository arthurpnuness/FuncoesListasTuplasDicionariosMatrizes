'''Peça ao usuário para digitar uma sequência de 10 números. Em seguida, crie duas listas a partir desta sequência: uma contendo os números pares e outra contendo os números ímpares.'''

lista = []
contador = 0
pares = []
impares = []

while contador < 10:

    numbers = int(input('Digite um numero: '))
    lista.append(numbers)
    contador += 1

for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('Numeros pares: ', pares)
print('Numeros impares: ', impares)
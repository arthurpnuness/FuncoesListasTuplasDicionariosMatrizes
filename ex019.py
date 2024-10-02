'''Dada a matriz numeros = [[2, 4], [6, 8]], calcule e imprima a soma de todos os elementos.'''

# Definindo a matriz
numeros = [[2, 4], [6, 8]]

# Inicializando a soma
soma = 0

# Percorrendo a matriz para somar os elementos
for linha in numeros:
    for elemento in linha:
        soma += elemento

# Imprimindo a soma
print("A soma de todos os elementos é:", soma)

'''Peça ao usuário para digitar duas sequências de 5 números e armazene em duas listas distintas. Após, faça um programa que junte essas duas listas em uma só.'''


contador = 0
lista1 = []  # Lista para armazenar os números
lista2 = []
num1 = []
num2 = []

while contador < 5:  # Alterado para contar até 5 números
    num1 = int(input('Digite um numero: '))
    num1.append(lista1)  # Adiciona cada número à lista
    contador += 1
    num2 = int(input('Digite outra sequencia de numero: '))
    num2.append(lista2)  # Adiciona cada número à lista
    contador += 1

concatenacao = lista1 + lista2

print(f'A juntas listas juntas ficam assim: {concatenacao}')
    
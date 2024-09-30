'''Escreva uma função chamada maior_numero que receba uma lista de números como parâmetro e retorne o maior número da lista. Teste a função com diferentes listas de números.'''

lista = []

def maiorNumero(lista):
    
    contador = 0
    
    while contador < 8:
        numeros = int(input('Digite um numero: '))
        lista.append(numeros)
        contador += 1
    
    return max(lista)

maior = maiorNumero(lista)
print(f'Voce me passo a seguinte lista {lista} e o maior numero dela é {maior}')

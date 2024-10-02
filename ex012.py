'''Escreva uma função chamada numeros_pares que receba uma lista de números e retorne uma nova lista contendo apenas os números pares da lista original.'''


# Criação da lista original com números de 1 a 16
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Definição da função numerosPares que recebe uma lista como parâmetro
def numerosPares(lista):
    # Criação de uma nova lista para armazenar os números pares
    novaLista = []
    
    # Laço que percorre cada número na lista original
    for numero in lista:
        # Verifica se o número é par
        if numero % 2 == 0:
            # Se for par, adiciona à nova lista
            novaLista.append(numero)
    
    # Retorna a nova lista com os números pares
    return novaLista

# Chama a função numerosPares e armazena o resultado na variável resultado
resultado = numerosPares(lista)

# Exibe o resultado no terminal
print(f'Está é a lista original: {lista}')
print(f'Está é a lista dos numeros pares: {resultado}')


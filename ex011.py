'''Escreva uma função chamada contar_elementos que receba uma lista e um elemento como parâmetros e retorne a quantidade de vezes que o elemento aparece na lista.'''

# Lista de exemplo
minhaLista = [1, 2, 3, 4, 3, 2, 3, 1, 3]

# Função para contar elementos
def contarElementos(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

# Chamando a função
elementoAcontar = 3
resultado = contarElementos(minhaLista, elementoAcontar)

print(f"O elemento {elementoAcontar} aparece {resultado} vezes na lista.")

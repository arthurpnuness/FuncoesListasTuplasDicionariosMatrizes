'''Escreva uma função chamada maior_numero que receba uma lista de números como parâmetro e retorne o maior número da lista. Teste a função com diferentes listas de números.'''

# Inicializa uma lista vazia para armazenar os números fornecidos pelo usuário
lista = []

# Define uma função chamada 'maiorNumero' que recebe uma lista como argumento
def maiorNumero(lista):
    
    # Inicializa um contador para controlar o número de entradas do usuário
    contador = 0
    
    # Usa um laço 'while' para solicitar 8 números do usuário
    while contador < 8:
        # Pede ao usuário para inserir um número e converte para inteiro
        numeros = int(input('Digite um numero: '))
        
        # Adiciona o número digitado pelo usuário à lista
        lista.append(numeros)
        
        # Incrementa o contador para acompanhar quantos números foram inseridos
        contador += 1
    
    # Retorna o maior número da lista usando a função 'max()'
    return max(lista)

# Chama a função 'maiorNumero' e armazena o maior número na variável 'maior'
maior = maiorNumero(lista)

# Exibe a lista fornecida pelo usuário e o maior número encontrado
print(f'Voce me passou a seguinte lista {lista} e o maior numero dela é {maior}')

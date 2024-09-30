'''Crie uma função chamada media que receba uma lista de números e retorne a média desses números. A média é calculada somando todos os números da lista e dividindo o total pelo número de elementos na lista.'''


# Define uma função chamada 'media' que calcula a média de uma lista de números
def media():
    
    # Inicializa uma lista vazia para armazenar os números fornecidos pelo usuário
    lista = []
    
    # Inicializa um contador para controlar o número de entradas do usuário
    contador = 0
    
    # Usa um laço 'while' para solicitar 6 números do usuário
    while contador < 6:
        # Pede ao usuário para inserir um número e converte para inteiro
        num = int(input('Digite um numero: '))
        
        # Adiciona o número digitado pelo usuário à lista
        lista.append(num)
        
        # Incrementa o contador para acompanhar quantos números foram inseridos
        contador += 1
    
    # Calcula a média dos números na lista. O denominador deveria ser 6, já que são 6 números
    m = sum(lista) / 6 

    # Exibe a lista fornecida pelo usuário e a média calculada
    print(f'Voce digitou os seguinte numeros {lista} e a media entre eles é: {m}')

# Chama a função 'media' para ser executada
media()
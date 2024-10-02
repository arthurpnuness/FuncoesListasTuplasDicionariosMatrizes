'''Escreva uma função chamada fibonacci que receba um número n e retorne uma lista contendo os n primeiros números da sequência de Fibonacci. A sequência de Fibonacci começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.'''

# "Fn=Fn−1+Fn−2,n≥3"

def serieFibonacci():

    #laço para verificar se o numero é valido
    while True:
        # Pede para o usuario um numero inteiro 
        num = int(input('Digite um numero inteiro positivo: '))

        if num > 0:
            break
        else:
            print('Por favor, digite um numero maior que ZERO !!!!!')

    # Sequência de Fibonacci
    fibo = [0, 1]
    
    # Laço para fazer a sequencia de Fibonacci apartir do numero fornecido
    for i in range(2, num):
        fibo.append(fibo[-1] + fibo[-2])

    # Mostra a sequência até o número digitado
    print(f'Os numeros da sequencia de Fibonacci com {num} termos são: {fibo[:num]}')

    

serieFibonacci()
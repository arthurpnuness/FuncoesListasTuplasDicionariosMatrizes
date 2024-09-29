'''Peça ao usuário para digitar as idades de várias pessoas, até o usuário digitar o valor 0. Após, calcule a média das idades e apresente na tela.'''

# Início de um loop infinito para garantir que o código continue pedindo entradas até a condição de parada ser atendida
while True:

    # Solicita ao usuário a idade de três pessoas: Sabrina, Alice e Helena
    age1 = int(input('Digite a idade da Sabrina: '))
    age2 = int(input('Digite a idade da Alice: '))
    age3 = int(input('Digite a idade da Helena: '))

    # Verifica se alguma das idades digitadas é igual a 0
    # Se for, o loop é interrompido usando "break", o que para a execução do programa
    if age1 == 0 or age2 == 0 or age3 == 0:
        break

    # Caso todas as idades sejam maiores que 0, calcula-se a média das três idades
    elif age1 > 0 and age2 > 0 and age3 > 0:
        media = (age1 + age2 + age3) / 3  # Soma as idades e divide por 3 para calcular a média
        # Exibe a média das idades com uma casa decimal
        print(f'A Médida de idade entre as mulheres é de {media:.1f} anos')
        break  # Após exibir a média, o loop é interrompido

    # Caso as idades inseridas não sejam válidas (números negativos, por exemplo), exibe uma mensagem de erro
    else:
        print('Opção invalida!')

'''Peça ao usuário para digitar as idades de várias pessoas, até o usuário digitar o valor 0. Após, calcule a média das idades e apresente na tela.'''

while True:

    age1 = int(input('Digite a idade da Sabrina: '))
    age2 = int(input('Digite a idade da Alice: '))
    age3 = int(input('Digite a idade da Helena: '))

    if age1 == 0 or age2 == 0 or age3 == 0:
        break
    elif age1 > 0 and age2 > 0 and age3 > 0:
        media = (age1 + age2 + age3) / 3
        print(f'A Médida de idade entre as mulheres é de {media:.1f} anos')
        break
    else:
        print('Opção invalida!')
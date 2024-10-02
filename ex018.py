'''Crie uma matriz 3x3 que represente um tabuleiro de jogo da velha, preenchendo com espaços vazios " ". Depois, marque um "X" na posição central e imprima a matriz.'''

# Criando a matriz 3x3 com espaços vazios
tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

# Marcando um "X" na posição central
tabuleiro[1][1] = "X"

# Imprimindo a matriz
print(tabuleiro[0][0] + "|" + tabuleiro[0][1] + "|" + tabuleiro[0][2])
print("-----")
print(tabuleiro[1][0] + "|" + tabuleiro[1][1] + "|" + tabuleiro[1][2])
print("-----")
print(tabuleiro[2][0] + "|" + tabuleiro[2][1] + "|" + tabuleiro[2][2])

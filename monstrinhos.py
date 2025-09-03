'''
Tarefa 02 - CF OBI 2024
2025.09.03
Luiz Otávio de Souza Freo
'''

# Objetivo: Ler os valores correspondentes à quantidade de Fadas (F) e Monstrinhos (M) que existem em um jogo, ler também os valores correspondentes à força de cada Monstrinho e de cada Fada, e além disso ler o bônus de cada Fada (a quantidade de vezes que cada uma delas pode lutar), e por fim determinar qual é o maior número de monstrinhos que podem ser derrotados se o jogo for jogado da melhor forma possível

# Ler o número de monstrinhos (M) e o número de fadas (F)
M = int(input())
F = int(input())

# Ler a força de cada monstrinho, a força de cada fada, e o bônus de cada fada
PM = []     # criando a lista dos mostrinhos
PF = []     # criando a lista das fadas

for i in range(M):  # lendo a força dos monstrinhos
    PM.append(int(input())) # armazenando o valor lido na lista

for i in range(F):  # lendo a força das fadas
    PF += [[0,0]]   # Aumentando a lista das fadas para armazenar a força e o bônus de cada fada
    PF[i][0] = int(input()) # armazenando o valor lido na lista

for i in range(F):  # lendo o bônus das fadas das fadas
    PF[i][1] = int(input()) # armazenando o valor lido na lista

# Organizar as listas em ordem decrescente de acordo com a força de cada monstrinho e de cada fada
PM.sort(reverse=True)
PF.sort(reverse=True)

# Calcular o maior número de monstrinhos que podem ser derrotados
V = 0   # variável para contar a qtd de vitórias

for i in range(M):  # verificando para cada monstrinho
    if PF[0][0] > PM[i]:    # testa se a força da fada mais forte é maior que a força do monstrinho que está sendo verificado
        V += 1          # caso retorne True (Verdade); adiciona 1 a vitórias
        PF[0][1] -= 1   # tira 1 do bônnus da fada
    if PF[0][1] == 0:       # testa se o bônus da fada mais forte acabou
        PF.pop(0)       # caso retorne True (Verdade); elimina a fada do jogo

# Mostrar a msg
print(V)

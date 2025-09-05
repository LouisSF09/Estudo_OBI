'''
Tarefa 02 - CF OBI 2023
2025.09.03
Luiz Otávio de Souza Freo
'''

# Objetivo: Ler um valor N, a quantidade de copos de suco, e a seguir ler N pares de números A e B, indicando se o suco é de abacaxi com hortelã (A), e se o suco possui pedacinhos (B), dessa forma, determinar quantos copos de suco não estão contaminados, ou seja, podem ser bebidos, considerando que para um suco ser contaminado A precisa ser igual a 0 (não pode ser de abacaxi com hortelã) e B precisa ser igual a 1 (precisa ter pedacinhos)

# Ler o valor N
N = int(input())

# Determinar quantos copos de suco podem ser bebidos
cont = 0   # variável dos copos de suco contaminados

for i in range(N):      # repete N vezes
    A, B = map(int, input().split())    # lê os valores A e B

    if (A == 0) and (B == 1):    # testa se os copos estão contaminados, pois um copo é contaminado se --> A == 0 e B == 1
        cont += 1      # caso retorne True (Verdade); conta 1 em cont (copos contaminados)

# Mostra a quantidade de copos que não estão contaminados
print(N - cont)

'''
Tarefa 01 - CF OBI 2024
2025.09.03
Luiz Otávio de Souza Freo
'''

# Objetivo: Ler um valor M, a idade em meses de uma árvore, determinar a altura da árvore em caixas após os M meses, e mostrar o resultado em uma msg

# Ler um valor M
M = int(input())

# Determinar a altura da árvore
if M <= 2:      # testa se a árvore tem 1 ou 2 meses
    C = M       # caso retorne True (Verdade); a altura da árvore em caixas é igual ao número de meses

elif M <= 4:    # caso retorne False (Falso); testa se a árvore tem 3 ou 4 meses
    C = M + 1   # caso retorne True (Verdade); a altura da árvore em caixas é igual ao número de meses mais 1

elif M == 5:    # caso retorne False (Falso); testa se árvore tem 5 meses
    C = 7       # caso retorne True (Verdade); a altura da árvore em caixas é igual a 7

else:    # caso retorne False (Falso); a idade da árvore é de 6 ou mais meses
    C = 7 + 6 * (M - 5) # realiza o cálculo atráves da fórmula: 7 (altura aos 5 meses) + 6 (altura que cresce a partir dos 5 meses) * (M - 5 (a qtd de meses após o mês 5))

# Mostrar o resultado em uma msg
print(C)

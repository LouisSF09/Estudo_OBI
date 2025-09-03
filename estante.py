'''
Tarefa 01 - CF OBI 2023
2025.09.03
Luiz Otávio de Souza Freo
'''

# Objetivo: Ler os valores X, Y, Z (o número de livros em diferentes pilhas) e N (o número de prateleiras existentes), e determinar qual é a menor quantidade de livros que precisam ficar fora das prateleiras para que estas possuam a mesma quantidade de livros

# Ler os valores
X, Y, Z, N = map(int, input().split())  # lê os valores atráves da função .split() e utiliza o map para já converter esses valores em inteiros

# Determinar a menor quantidade de livros que precisam ficar fora das prateleiras
L = (X + Y + Z) % N     # soma os livros que estão nas 3 estantes, divide pelas N prateleiras, e armazena o resto da divisão (resto dos livros) na variável L

# Mostra o resultado
print(L)

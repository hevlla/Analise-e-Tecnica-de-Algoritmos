baralho = list()
""""
Falta criar exceção para qtd_cartas == 1 e terminar a distribuição das cartas
"""

def cria_cartas(qtd_cartas):
    globals(baralho)
    for carta in range(qtd_cartas):
        carta += 1
        baralho.append(carta)
    return baralho

def distribuindo_cartas():
    cartas_descartadas = list()
    #while len(baralho) != 1:
        

while True:
    qtd_cartas = int(input())
    if qtd_cartas == 0 or qtd_cartas > 50:
        break
    print(cria_cartas(qtd_cartas))

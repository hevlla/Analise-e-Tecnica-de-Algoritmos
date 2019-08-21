baralho = list()

def cria_cartas(qtd_cartas):
    for carta in range(qtd_cartas):
        carta += 1
        baralho.append(carta)
    return baralho

def distribuindo_cartas():
    cartas_descartadas = list()
    if len(baralho) == 1:
        return cartas_descartadas
    while len(baralho) != 1:
        cartas_descartadas.append(baralho[0])
        baralho.pop(0)
        baralho.append(baralho[0])
        baralho.pop(0)
    return cartas_descartadas



while True:
    qtd_cartas = int(input())
    if qtd_cartas == 0 or qtd_cartas > 50:
        break
    cria_cartas(qtd_cartas)
    print("Discarded cards: ", distribuindo_cartas(), "\nRemaining card: ", baralho)

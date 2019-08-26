baralho = list()
cartas_descartadas = list()

def cria_cartas(qtd_cartas):
    baralho.clear()
    for carta in range(1, qtd_cartas+1):
        baralho.append(carta)
    return baralho

def distribuindo_cartas():
    cartas_descartadas.clear()
    while len(baralho) != 1:
        cartas_descartadas.append(str(baralho[0]))
        baralho.pop(0)
        baralho.append(str(baralho[0]))
        baralho.pop(0)

def main():
    while True:
        qtd_cartas = int(input())
        if qtd_cartas == 0 or qtd_cartas > 50:
            break
        cria_cartas(qtd_cartas)
        distribuindo_cartas()
        print("Discarded cards: " +", ".join(cartas_descartadas), end="")
        print("\nRemaining card:", str(baralho[0]), end="\n")

if __name__ == "__main__":
    main()

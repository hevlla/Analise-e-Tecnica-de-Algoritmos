while True:
  qtd_cartas = int(input())  
  manter_cartas = []
  descartar_cartas = []

  if qtd_cartas == 0:
    break

  for i in range(qtd_cartas):
    manter_cartas.append(i+1)

  while len(manter_cartas) > 1:
    descartar_cartas.append(str(manter_cartas.pop(0)))
    manter_cartas.insert(len(manter_cartas) - 1, manter_cartas.pop(0))

  print("Discarded cards: " + ", ".join(descartar_cartas), end="")
  print("\nRemaining card: " + str(manter_cartas[0]), end="\n")



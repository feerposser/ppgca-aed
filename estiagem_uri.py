
n_cidade = 0

while True:
    x = int(input())
    consume = []
    total_consume, total_people = 0, 0

    if x == 0:
        break

    for x in range(0, x):
        auxiliar = input()
        consumo, pessoas = int(auxiliar[auxiliar.find(' '):]), int(auxiliar[:auxiliar.find(' ')+1])
        total_consume += int(consumo)
        total_people += int(pessoas)
        consumo = int(consumo) // int(pessoas)
        consume.append([pessoas, consumo])
    total_consume = total_consume/total_people

    consume = sorted(consume, key=lambda consume: consume[1])

    n_cidade += 1

    total_consume = list(str(int(total_consume*100)))
    total_consume.insert(-2, ".")
    total_consume = str().join(total_consume)

    aux = ""
    for i in consume:
        aux += str(i[0]) + "-" + str(i[1]) + " "
    aux = aux[:-1]

    print("Cidade# %s:" % n_cidade)
    print(aux)
    print("Consumo medio: %s m3." % total_consume)

    print("")



import time

from memory_profiler import profile

@profile
def teste():
    from random import randint

    start_time = time.time()
    n_cidade = 0

    for i in range(0, randint(1, 106)):
        qtd_casas = randint(1, 10)
        consume = []
        total_consume, total_people = 0, 0

        if qtd_casas == 0:
            break

        for qtd_casas in range(0, qtd_casas):
            total_people, consumo = (randint(1, 10), randint(1, 200))
            total_consume += consumo
            consumo = consumo // total_people
            consume.append([total_people, consumo])
        total_consume = total_consume / total_people

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

    print("--- %s  seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    teste()

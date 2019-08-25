
info_cities = []
n_cidade = 0

def separa(s):
    """
    feito para testar se o problema não está no split do URI
    :param s: string com espaço
    :return:
    """
    return int(s[s.find(' '):]), int(s[:s.find(' ')+1])

while True:
    x = int(input())
    info_cities = []
    consume = []
    total_consume, total_people = 0, 0

    if x == 0:
        # print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        break

    for x in range(0, x):
        auxiliar = input()
        consumo, pessoas = separa(auxiliar)
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


    # info_cities.append([n_cidade, aux, total_consume])

    # for i in range(0, len(info_cities)):
    print("Cidade# %s:" % n_cidade)
    print(aux)
    print("Consumo medio: %s m3." % total_consume)

    print("-")



# for i in range(0, len(info_cities)):
#     print(info_cities[i][0])
#     print([(print(*x)) for x in info_cities[i][1]])
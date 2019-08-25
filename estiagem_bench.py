from random import randint

count = 0
print('--começo')

while count < 106:
    qtd_casas = randint(1, 10)

    print(qtd_casas)
    for i in range(0, qtd_casas):
        qtd_pessoas = randint(1, 10)
        qtd_consumo = randint(1, 200)
        print(qtd_pessoas, qtd_consumo)
    count += 1
print(0)
print('--fim')
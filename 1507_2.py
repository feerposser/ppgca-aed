"""
PROFESSOR, NÃO LEVAR ESTE CÓDIGO EM CONSIDERAÇÃO
"""


qtd_testes = int(input())

for i in range(0, qtd_testes):
    string_testada = input()
    qtd_substrings = int(input())

    for j in range(0, qtd_substrings):
        substring = input()
        indice = 0
        achou = False

        for c in string_testada:
            print('string testada', string_testada, 'c', c, 'substring', substring, 'substring[indice]', substring[indice])
            if c == substring[indice]:
                # print('oo')
                indice += 1

            if indice == len(substring):
                # print('UU')
                achou = True
                break

        if achou:
            print('Yes')
        else:
            print('No')

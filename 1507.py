
def subsequencia(index, sequencia, sub):
    # print("index:", index, "sequencia:", sequencia, "sub:", sub)
    encontrado = sequencia[index:].find(sub)

    if encontrado < 0:
        # print("não achou", encontrado)
        return -1
    # print('achou', encontrado, 'retornando:', encontrado+index)
    return encontrado + index


for i in range(0, int(input())):
    sequencia = str(input())

    sub = []
    for i in range(0, int(input())):
        sub.append(input())

    for i in sub:
        index = 0
        verifica = False

        for j in range(0, len(i)):
            # print('\n', i, ':', j, ':', i[j], '-')
            # print('\tvalor do index:', index)

            if index >= len(sequencia):
                # print('\tcaiu no primeiro break')
                print('No')
                break

            aux = subsequencia(index, sequencia, i[j])
            # print('\tvalor de aux:', aux)
            if aux >= 0:
                # print('\tcaiu no if aux')
                index = aux + 1
            else:
                # print(i, i[j], sequencia[index:], aux)
                verifica = True
                break
        if verifica:
            print('No')
        else:
            print('Yes')
# print("")


for i in range(0, int(input())):
    sequencia = str(input())

    for j in range(0, int(input())):
        subseq = input()
        index_seq = 0
        status = True

        for s in subseq:
            find = sequencia[index_seq:].find(s)
            if find < 0:
                status = False
                break
            else:
                index_seq += find + 1

        if status:
            print("Yes")
        else:
            print("No")



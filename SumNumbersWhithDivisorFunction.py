def fdivisor(down, up, divisor):
    list = []
    for i in range(int(down), int(up)+1):
        if i % divisor == 0:
            list.append(i)
    summa = sum(list)
    print (summa)

fdivisor(1, 1000, 7)
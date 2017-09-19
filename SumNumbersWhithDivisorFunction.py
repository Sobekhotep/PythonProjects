def fdivisor(down, up, divisor):
    list = []
    for i in range(int(down), int(up)+1):
        if i % divisor == 0:
            list.append(i)

    print (sum(list))

fdivisor(1, 1000, 17)
fdivisor(1, 1000, 21)
fdivisor(1, 1000, 33)
fdivisor(1, 1000, 47)
fdivisor(1, 1000, 55)
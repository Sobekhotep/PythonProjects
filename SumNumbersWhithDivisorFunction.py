def fdivisor(down, up, divisor):
    a = 0
    for i in range(int(down), int(up)+1):
        if i % divisor == 0:
            a = a + i
    return a

print(fdivisor(1, 1000, 17))
print(fdivisor(1, 1000, 21))
print(fdivisor(1, 1000, 33))
print(fdivisor(1, 1000, 47))
print(fdivisor(1, 1000, 55))
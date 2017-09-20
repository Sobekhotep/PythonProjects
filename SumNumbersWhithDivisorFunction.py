def fdiv(down, up, div):
    a = 0
    for i in range(down, up+1):
        if i % div == 0:
            a = a + i
    return a

print(fdiv(1, 1000, 17))
print(fdiv(1, 1000, 21))
print(fdiv(1, 1000, 33))
print(fdiv(1, 1000, 47))
print(fdiv(1, 1000, 55))
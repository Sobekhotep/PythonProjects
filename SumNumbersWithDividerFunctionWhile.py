def fdivider(down, up, div):
    var = 0
    var2 = 0

    while var < up:
        var += down
        if var % div == 0:
            var2 += var

    return var2

print(fdivider(1, 1000, 17))
print(fdivider(1, 1000, 21))
print(fdivider(1, 1000, 33))
print(fdivider(1, 1000, 47))
print(fdivider(1, 1000, 55))
def fdivider(down, up, div):
    local_sum = 0
    total_sum = 0

    while local_sum < up:
        local_sum += down
        if local_sum % div == 0:
            total_sum += local_sum

    return total_sum

print(fdivider(1, 1000, 17))
print(fdivider(1, 1000, 21))
print(fdivider(1, 1000, 33))
print(fdivider(1, 1000, 47))
print(fdivider(1, 1000, 55))
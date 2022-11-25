def digital_root(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n

n = 10
print(digital_root(n))

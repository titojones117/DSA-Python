def bits(n):
    return list(2**i for i in range(n+1))
print(bits(16))
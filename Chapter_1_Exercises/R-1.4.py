def square(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i
    return sum

print(square(9))
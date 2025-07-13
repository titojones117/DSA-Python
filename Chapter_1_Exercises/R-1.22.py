import random

def dot_product(data1, data2):
    data3 = []
    if len(data1) == len(data2):
        for i in range(0,len(data1)):
            data3.append(data1[i]*data2[i])
    else:
        return print("data sets are not of the same length")
    return data3

n = 5

A = [random.randint(0,10) for _ in range(n+1)]
B = [random.randint(0,10) for _ in range(n+1)]

print(f"A = {A}\nB = {B}\n")
print(f"Dot Product of A & B = {dot_product(A,B)}")

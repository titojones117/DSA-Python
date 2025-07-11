def arithmetic(a,b,c):
    if (a+b == c):
        return f"{a} + {b} = {c} is true"
    elif (b - c == a):
        return f"{a} = {b} - {c} is true"
    elif (a*b == c):
        return f"{a}*{b} = {c} is true"
    else:
        return f"you failed :("

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

print(arithmetic(a,b,c))

def aretheydiff(data):
    return len(set(data))==len(data)

print(aretheydiff([1,2,3,4,5,6,6]))
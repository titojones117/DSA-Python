def minmax(data):

    smallest = largest = data[0]
    for num in data:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num
    return  (smallest, largest)

print(minmax([0,1,2,34,5,6,7]))
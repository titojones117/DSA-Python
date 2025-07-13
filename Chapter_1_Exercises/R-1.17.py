def scale(data, factor):
    for val in data:
        val *= factor

data = [1,2,3,45,6,7,6,7,76]
factor = 10

print(scale(data, factor))

# No, this implementation does not work as intended.
# Why?
# When we create the variable val, we are creating a
# temporary value that holds the same value as the
# element from the list.
# We are not mutating the actual elements within our list
# like we do when we compute data[i] *= factor. 

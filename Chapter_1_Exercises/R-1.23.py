data = [0,1,2,3,4,5]

try:
    data[99] = 1 # Try to add the integer 1 to index 99 of data.
except IndexError:
    print("Don't try buffer overflow attacks in Python!")

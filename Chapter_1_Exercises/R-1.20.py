from random import randint

def custom_shuffle(data):
    for i in range(len(data)):
        j = randint(0, i)
        data[i], data[j] = data[j], data[i]

my_list = [1, 2, 3, 4, 5, 6, 7]
custom_shuffle(my_list)
print(my_list)  # Now you'll see the shuffled result!

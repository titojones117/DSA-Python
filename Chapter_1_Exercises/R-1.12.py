from random import randrange

def custom_choice(data):
    index = randrange(len(data))
    return data[index]

print(custom_choice([10,101,20,40,10]))
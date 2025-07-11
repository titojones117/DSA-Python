# count the number of vowels in a string

def vowels(word):
    count = 0
    for character in word:
        if character in "AaIiEeOoUu":
            count += 1
    return [count, word]
    
name = input("Whats your name?: ")
print(vowels(name))
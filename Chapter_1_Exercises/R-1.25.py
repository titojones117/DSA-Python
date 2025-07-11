def remove_punctuation(s):
    return ''.join(char for char in s if char.isalnum() or char.isspace())


print(remove_punctuation("Fuck you you fucking idiot! I can't stand this shit anymore!"))
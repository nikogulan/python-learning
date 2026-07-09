snake_case = input("What is your name in camelCase? ")
scase = ""
for char in snake_case:
    if char.isupper():
        scase += "_" + char.lower()
    else:
        scase += char

print(scase)



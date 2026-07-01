expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

if y == "+":
    sum = x + z
    print(float(sum))
elif y == "-":
    subtract = x - z
    print(float(subtract))
elif y == "*":
    multi = x * z
    print(float(multi))
elif y == "/":
    div = x / z
    print(float(div))
else:
    print("Wrong Input!")


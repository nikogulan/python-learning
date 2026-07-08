while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if x > y:
            continue
        elif x < 0 or y <= 0:
            raise ValueError
        else:
            result = round((x / y) * 100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if result >= 99:
    print("F")
elif result <= 1:
    print("E")
else:
    print(f"{result}%")

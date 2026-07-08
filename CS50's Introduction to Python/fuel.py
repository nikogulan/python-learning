def main():

    while True:
        try:
            fraction = input("Fraction: ")
            splitted = fraction.split("/")
            x = int(splitted[0])
            y = int(splitted[1])
            if x > y:
                continue
            elif x < 0 or y <= 0:
                raise ValueError
            else:
                result = int((x / y) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    if rounded_result >= 99:
        print("F")
    elif rounded_result <= 1:
        print("E")
    else:
        print(f"{rounded_result}%")


main()

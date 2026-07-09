def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and s[0:2].isalpha():

        for char in s:
            if char.isnumeric():
                index = s.index(char)
                if s[index:].isnumeric() and char != "0":
                    return True
                else:
                    return False
        return True

    else:
        return False

main()

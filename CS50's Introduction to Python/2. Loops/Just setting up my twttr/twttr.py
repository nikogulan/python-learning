def main():
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    inp = input("Input: ")

    for i in vowels:
        res = "".join(vowels)

        for char in res:

            if char in inp:
                inp = inp.replace(char, "")

    print(f"Output: {inp}")

main()

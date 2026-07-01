greeting = input("Greeting: ").lower().strip()
first_letter = greeting[0]


if greeting == "hello":
    print("$0")
elif first_letter == "h" and "hello" in greeting:
    print("$0")
elif first_letter == "h":
    print("$20")
else:
    print("$100")


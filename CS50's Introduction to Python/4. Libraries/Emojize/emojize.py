import emoji

user_input = input("Input: ")
emojized = emoji.emojize(user_input, language="alias")
print(f"Output: {emojized}")

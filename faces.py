def convert(user_str):
    return user_str.replace(":)", "🙂").replace(":(", "🙁")


text = input("Write something with smile or sad emoticon at the end ")

print(convert(text))


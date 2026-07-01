answer = input("What is the Aswer to the Great Question of Life, the Univers and Everything? ")
answerLow = answer.lower().strip()

if answerLow == "42" or answerLow == "forty-two" or answerLow == "forty two":
    print("Yes")
else:
    print("No")

print("Quiz!")

playing = input("Do you want to play? Type yes(Y) or no(N) to continue: \n")
firstQuestion = "How would you define this example?\n"
counter = 0

if playing!="Y":
    quit()

print(firstQuestion)
firstAnswer =  input("Pretty dumb(a)\nAn opportunity to learn(b)\nSmart(c)\n")

if firstAnswer=="b":
    counter=counter+1

if counter!=0:
    print("Good Answer")
else:
    print("Change your mentality about it, or you won't move forward")


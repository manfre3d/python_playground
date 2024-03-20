import random

options =["rock","paper","scissors"]

while True:
    user_input = input("Choose between rock, paper, scissors or type x to quit the game: \n").lower()
    print("user input: "+user_input+"\n")
    if user_input == 'x':
        break

    if user_input not in options:
        continue

    random_num = random.randint(0,2)
    # 0 rock 1 paper 2 scissors
    print("computer: "+options[random_num]+"\n")
    if user_input== "rock" and options[random_num]=="scissors":
        print("we won!")
    elif user_input== "paper" and options[random_num]=="rock":
        print("we won!")
    elif user_input== "scissors" and options[random_num]=="paper":
        print("we won!")
    else:
        print("we lost")



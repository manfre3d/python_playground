import random

rand = random.randint(1,6)

# print(rand)
user_input = input("Guess a number between 1 and 5:\n")
if user_input.isdigit():
    user_input = int(user_input)
while user_input!=rand:
    adjustement_for_user =""
    if int(user_input)<rand:
        adjustement_for_user="try an higher number" 

    if int(user_input)>rand:
      adjustement_for_user="try a lower number" 

    user_input = input("Guess again!\nSuggestione: "+adjustement_for_user+" (remember the number is between 1 and 5) :\n")
    if user_input.isdigit():
        user_input =int(user_input)

print("Correct!")

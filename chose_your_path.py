

name = input("What's your name stranger? \n")

print("Hi! "+name+" welcome to this very breath journey! \nWe are going to move forward towards a goal and you'll have to pick the correct way to reack the end!\nHow do you wish to move forward in this journey? \n")
continue_game = True
while continue_game:
    beginGame = input("first of all, want to play the game? 'q to leave anything else to continue'")

    if beginGame =='q':
        break

    firstChoice = input("write one of the options to move forward:\n 'one step at a time' 'running' 'I'll consider my options first'")

    if firstChoice=='one step at a time':
        secondChoice =input("You start slow and you don't really see many results, what do you do now? 'keep going' 'stop it's not working' 'try to do more'")

        if secondChoice == "keep going":
            print("That's a good choice, slow and steady will always win the race! Stay consistent")
        elif secondChoice == "stop it":
            print("That's a great way! to not move forward at all.. think about it, change your point of view and \ngo for it as slow or fast as you need. You can do it!")
        elif secondChoice == "try to do more":
            print("don't stress to much and try to focus on quality over quantity,\n doing the same thing wrong won't get you a different result unless you take the right amount of time to improve")

    elif firstChoice == 'running' :
        secondChoice =input("You start fast but you are having difficulties understanding some of the subjects you quickly went over. What can you do to ammend that?\n 'slow down' 'take a moment to think' 'both'")
        if secondChoice=="both":
            print("it's good to do both, the solution often isn't unilateral! slowing down without re evalueting may lead to a blockage and thinking too much can have the same effect, make a plan! You can do it!")
        elif secondChoice=='slow down'or secondChoice== 'take a moment to think':
            print("this may lead to a blockage take the time that you need to move forward with a plan, no one is chasing you!\nfocus on moving forward bit by bit.")

    elif firstChoice == "I'll consider my options first":
        print("thinking often feels like you are doing more that you actually are, take action!")
    else:
        print("invalid choice brother, think again on how you can move towards your goal")
    
    continue_input= input("\n\ndo you wish to try again? Press Y to continue N to quit:\n")
    if continue_input=="Y":
        continue
    else:
        continue_game = False
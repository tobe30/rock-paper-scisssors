#never win version of rock paper scissors by marizu
import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper" , "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)
    
    if user_input == "exit" :
        print("Game ended")
        if user_points < computer_points:
            print("computer won a total score of "+str(computer_points)+" and the user total score is " +str(user_points))
        elif user_points > computer_points:
            print("You won a total score of "+str(user_points)+" and the computer total score is " +str(computer_points))

        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("computer input is rock")
            print("It is a tie!")
        elif computer_input == "paper":
            print("Your input is rock")
            print("computer input is paper")
            print(" computer wins")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock")
            print("computer input is paper")
            print("computer win")
            print(computer_input.replace("scissors", "paper"))
            computer_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print(computer_input.replace("rock", "scissors"))
            print("computer input is scissors")
            print("computer win!")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is paper")
            print("computer input is paper")
            print("it's a tie!")
        elif computer_input == "scissors":
            print("Your input is paper")
            print("computer input is scissors")
            print("computer wins")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("computer input is rock")
            print("computer win!")
            computer_points += 1
        elif computer_input == "paper":
            print(computer_input.replace("paper", "rock"))
            print("computer input is rock")
            print("computer win")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("computer input is scissors")
            print("its a tie")
    elif user_input == "exit":
        print()

    elif user_input != " rock" or user_input != "paper" or user_input != "scissors" and user_input != "exit":
        print("Invalid Input")

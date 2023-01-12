import random
user_win = 0
computer_win = 0


def choose_option():
    user_choice = input(" Choose Rock or Paper or Scissor?")
    if user_choice in ["Rock", "rock", "r"]:
       user_choice = "rock"
    elif user_choice in ["Paper", "paper", "p"]:
         user_choice = "paper"
    elif user_choice in ["Scissor", "scissor", "s"]:
         user_choice = "scissor"
    else:
        print("I don't know")
        choose_option()
    return user_choice


def computer_option():

    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
       computer_choice = 'rock'

    elif computer_choice == 2:
       computer_choice = 'paper'

    elif computer_choice == 3:
       computer_choice = 'scissor'
    return computer_choice

while True:
    print("")
    computer_choice = computer_option()
    user_choice = choose_option()
    print("")

    if user_choice == "rock":
        if computer_choice == "rock":
            print("It is a tie")
        elif computer_choice == "paper":
            print("You lose!", computer_choice, "covers", user_choice)
            computer_win += 1
        elif computer_choice == "scissor":
            print("You win!", user_choice, "smashes", computer_choice)
            user_win += 1

    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!", user_choice, "covers", computer_choice)
            user_win += 1
        elif computer_choice == "paper":
            print("It's tied")
        elif computer_choice == "scissor":
            print("You lose...", computer_choice, "smashes", user_choice)
            computer_win += 1

    elif user_choice == "scissor":
        if computer_choice == "rock":
            print("You lose...", computer_choice, "smashes", user_choice)
            computer_win += 1
        elif computer_choice == "scissor":
            print(" It's tied")
        elif computer_choice == "paper":
            print("You win!", user_choice, "covers", computer_choice)
            user_win += 1
    print("")
    print("User Win: " + str(user_win))
    print("Computer Win: " + str(computer_win))
    print("")
    user_choice = input("Do you want to play again? yes/no?")
    if user_choice in ["Y", "y", "yes"]:
        pass
    elif user_choice in ["N", "n", "no"]:
        break

    else:
        break




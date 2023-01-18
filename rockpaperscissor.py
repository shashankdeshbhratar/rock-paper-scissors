import random
player_choice = int(input("Which number are you choosing? 0 for Rock or 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer choose {computer_choice}")
if player_choice >= 3 or player_choice < 0:
    print("You insert incorrect number, You lose.")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 1 and computer_choice == 0:
    print("You win")
elif player_choice == 2 and computer_choice == 1:
    print("You win")
elif computer_choice > player_choice:
    print("You lose")
elif computer_choice == player_choice:
    print("Its a draw")
else:
    print("You insert incorrect number, You lose.")

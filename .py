import random

print("--Welcome to Rock, Paper and Scissors--")
print()

options = [ "rock", "paper", "scissors", "laser gun"]

# Get user input
user_input = input("Enter rock, paper, or scissors: ").lower()

# Validate user input
if user_input not in options:
    print("Invalid choice! Please enter rock, paper, or scissors.")
else:
    # Computer makes a random choice
    computer_choice = random.choice(options)
    print(f"You chose: {user_input}")
    print(f"Computer chose: {computer_choice}")
    print()
    
    # Determine winner
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper") or \
         (user_input == "laser gun" and computer_choice == "rock") or \
         (user_input == "laser gun" and computer_choice == "paper") or \
         (user_input == "laser gun" and computer_choice == "scissors"):
        print("You win!")
    else:
        print("You lose!")  

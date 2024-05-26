import random

# Define the choices and rules
choices = ["rock", "paper", "scissors", "lizard", "spock"]
rules = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

def get_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif choice2 in rules[choice1]:
        return f"{choice1.capitalize()} beats {choice2}! You win!"
    else:
        return f"{choice2.capitalize()} beats {choice1}! You lose!"

def main():
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock) or 'quit' to exit: ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(user_choice, computer_choice)
        print(result)
        print()

if __name__ == "__main__":
    main()

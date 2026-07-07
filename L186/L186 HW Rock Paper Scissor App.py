import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Try again.")

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie"
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You win"
    return "You lose"

def play():
    print("=== Rock Paper Scissors ===")
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    print(decide_winner(user, computer))

if __name__ == "__main__":
    while True:
        play()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            break

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter your move (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Try again.")
        choice = input("Enter your move (rock, paper, scissors): ").lower()
    return choice

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    rounds = 5
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors! Best of 5 rounds.\n")
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}:")
        user_move = get_user_choice()
        computer_move = get_computer_choice()
        print(f"You chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        winner = decide_winner(user_move, computer_move)
        if winner == "user":
            print("You win this round!\n")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!\n")
            computer_score += 1
        else:
            print("This round is a tie!\n")

    print("\nFinal Results:")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Sorry, the computer won the game.")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    main()

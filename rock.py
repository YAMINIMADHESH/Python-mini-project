import random
print("✊ ✋ ✌ Rock, Paper, Scissors Game")
choices = ["rock", "paper", "scissors"]
while True:
    user=input("Enter rock, paper, or scissors (or q to exit): ").lower()
    if user == 'q':
        print('Game over. Byee👋')
        break
    if user not in choices:
        print("Invalid choice. Please try again.")
        continue
    com=random.choice(choices)
    print(f"Computer chose: {com}")
    if user == com:
        print("It's a tie! 🤝")
    elif (user == "rock" and com == "scissors") or \
         (user == "paper" and com == "rock") or \
         (user == "scissors" and com == "paper"):
        print("You win! 🎉")
    else :
        print("Computer wins! 💻")
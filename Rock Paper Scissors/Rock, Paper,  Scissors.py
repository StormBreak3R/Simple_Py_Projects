import random
options = ["Rock", "Paper", "Scissors"]
computer_score = 0
player_score = 0

for i in range(3):
    computer = random.choice(options)
    player = input("Rock, Paper or Scissors? -> ").capitalize()
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cut", computer)
            player_score += 1

print(f"Score: ")
print(f"Computer Score: {computer_score}")
print(f"Player Score: {player_score}")



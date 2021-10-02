import random  # importing random module
roll_again = "yes"

min_val = 1
max_val = 6

while roll_again == "yes" or roll_again == "y":  # while loop
    print("Rolling the Dice. . .")
    print("Values are: ")
    print(random.randint(min_val, max_val))  # using the random.radiant() function
    print(random.randint(min_val, max_val))
    print("You wanna roll again?")
    roll_again = input(": ").lower()
    if roll_again == "no" or roll_again == "n":  # condition to break the loop
        break


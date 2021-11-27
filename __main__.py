import random

# global strings
score = 0

# tricks
tricks = {
    "hop": {"score": 1, "chance": 3},
    "ollie": {"score": 5, "chance": 5},
    "kickflip": {"score": 10, "chance": 8},
    "nollie": {"score": 8, "chance": 7}
}

while True:
    print("********************************************")
    ask_trick = input("Which trick you want do to: ")
    if ask_trick == "hop":
        random_chance = random.randint(1, 100) - tricks["hop"]["chance"]
        if random_chance >= 15:
            score = score + tricks["hop"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))

    elif ask_trick == "ollie":
        random_chance = random.randint(1, 100) - tricks["ollie"]["chance"]
        if random_chance >= 15:
            score = score + tricks["ollie"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))

    elif ask_trick == "kickflip":
        random_chance = random.randint(1, 100) - tricks["kickflip"]["chance"]
        if random_chance >= 23:
            score = score + tricks["kickflip"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))
    elif ask_trick == "nollie":
        random_chance = random.randint(1, 100) - tricks["nollie"]["chance"]
        if random_chance >= 21:
            score = score + tricks["nollie"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))
    else:
        print(ask_trick + " that trick doesn't exist")

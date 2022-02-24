import random

# global strings
score = 0
bonus_chances = 0

# tricks
tricks = {
    "hop": {"score": 1, "chance": 3},
    "ollie": {"score": 5, "chance": 5},
    "kickflip": {"score": 10, "chance": 8},
    "nollie": {"score": 8, "chance": 7},
    "heelflip": {"score": 12, "chance": 10}
}
characters = {
    "Tony Hawk": "Chance is plus 5",
    "cj-thiel": "Chance is plus 3"
}
for row in characters:
    print(row)
chose_character = input('Chose character: ')

if chose_character == "Tony Hawk":
    bonus_chances = tricks["hop"]["chance"] + 1

while True:
    print("********************************************")
    ask_trick = input("Which trick you want do to: ")
    if ask_trick == "hop":
        random_chance = random.randint(1, 100) - tricks["hop"]["chance"] + bonus_chances
        if random_chance >= 15:
            score = score + tricks["hop"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))

    elif ask_trick == "ollie":
        random_chance = random.randint(1, 100) - tricks["ollie"]["chance"] + bonus_chances
        if random_chance >= 15:
            score = score + tricks["ollie"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))

    elif ask_trick == "kickflip":
        random_chance = random.randint(1, 100) - tricks["kickflip"]["chance"] + bonus_chances
        if random_chance >= 23:
            score = score + tricks["kickflip"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))
    elif ask_trick == "nollie":
        random_chance = random.randint(1, 100) - tricks["nollie"]["chance"] + bonus_chances
        if random_chance >= 21:
            score = score + tricks["nollie"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))
    elif ask_trick == "heelflip":
        random_chance = random.randint(1, 100) - tricks["heelflip"]["chance"] + bonus_chances
        if random_chance >= 25:
            score = score + tricks["heelflip"]["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is " + str(score))
    else:
        print(f"\"{ask_trick}\" that trick doesn't exist")

import random

#global strings
score = 0

# tricks
ollie = {
    "score": 5,
    "chance": 5
}
kickflip = {
    "score" : 10,
    "chance" : 8
}


while True:
    print("********************************************")
    ask_trick = input("Which trick you want do to: ")
    if ask_trick == "ollie":
        random_chance = random.randint(1, 100) - ollie["chance"]
        if random_chance >= 15:
            print(str(random_chance))
            score = score + ollie["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is: " + str(score))
    if ask_trick == "kickflip":
        random_chance = random.randint(1, 100) - kickflip["chance"]
        if random_chance >= 23:
            print(str(random_chance))
            score = score + kickflip["score"]
            print("You did it! Your score is " + str(score))
        else:
            print("Loser! Your score is: " + str(score))

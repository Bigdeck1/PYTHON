import random

def ikot():
    min_val = 1
    max_val = 6
    ikot = random.randint(min_val, max_val)

    return ikot

while True:
    manlalaro = input("Enter number of player (1-4): ")
    if manlalaro.isdigit():
        manlalaro = int(manlalaro)
        if 2 <= manlalaro <= 4:
            break
        else:
            print("Please enter a number between 1 and 4")
    else:
        print("Invalid input")
max_score = 50
manlalaro_scores = [0 for _ in range(manlalaro)]

while max(manlalaro_scores) < max_score:
    for manlalaro_idx in range(manlalaro):
        print("\nPlayer number",manlalaro_idx +  1, "turn has just started!\n")
        scores = 0

    while True:
        should_ikot = input("Do you want to roll again? (y/n): ")
        if should_ikot.lower() == "y":
            break
        val = ikot()
        if val == 1:
            print("rolled a 1! turn done!")
            scores = 0
        else:
            scores += val
            print("you rolled a:", val)
        print("score:", scores)

    manlalaro_scores[manlalaro_idx] += scores
    print("Your total score is:", manlalaro_scores[manlalaro_idx])
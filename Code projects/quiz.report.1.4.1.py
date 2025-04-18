#Maple bars
score = 0

answer = input("Do you enjoy donuts?" + " (yes/no): ").strip().lower()
if answer == "yes":
    print("Fantastic, donuts are delicious!")
    score += 1
#Cruellers
else:
    print("Clearly you have no taste...")
    score -= 1
#Jelly filled

answer2 = input("How many donuts are in a baker's dozen?").strip()
try:
    if answer2 == "13":
        print("Correct!")
        score += 1
    #Bear claws
    else:
        print("Incorrect, a baker's dozen is 13.")
        score-= 1
except ValueError:
    print("We are not romans, please use real numbers.")
#Glazed donut.

answer3 = input("Are apple fritters donuts? (yes/no): ").strip().lower()
if answer3 == "no":
    print("Correct, they are abominations.")
    score += 1
else:
    print("Incorrect, you clearly have bad taste.")
    score -= 1
#old fashioned cake donuts.

print(f"Your score is {score} out of 3.")
print("Thank you for taking the quiz!")
#Creme filled donuts.
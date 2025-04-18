name = input("What is your name?")
print(f"Welcome {name}.")#My brother is trying to impress the germans, so he gave me this for my birthday.
age = 33
print("You are", age, "years old.")
#Happy Birthday.
print("You are {} years old.".format(age))
#Thank you.
print(f"You are {age} years old.")
#Who you are working for?


wage = input("How much are you paid?") #changed age to wage to have different variable.
print(type(wage))
wage = int(wage)
print(type(wage))
print(wage * 7) 
#Blockbuster Video, Des Moisnes, Iowa
print(f"You are {wage * 7} in dog years.")
#Time out, I hate to break out of character, but you cannot shout into a person's ear.  

num = int(input("Enter a Number: "))
if num % 2 == 0:
    print("The Number is Even.")
elif num < 0:
    print("The Number is Negative.")
else: 
    print("The Number is Odd.")
#We do have to clean up after? Always

has_id = input("Do you have an ID? (yes/no) ").strip().lower() == 'yes'
if age >= 18 and has_id:
    print("Access Granted.")
else:
    print("Get lost, Nerd.")
#Get away from that phone!

has_license = input("Do you have your driver's license? (yes/no) ").strip().lower() == 'yes'
if age >= 25 and has_license:
    print("You can rent a car.")
else:
    print("Go for a walk.")
#What sort of work does your brother do?

score = 0
answer = input("Are donuts delicious? (yes/no) ").lower().strip()
#Film.
if answer == 'yes':
    score += 1
    print("Correct! Donuts are delicious.")
else:
    print("Incorrect. Donuts are indeed delicious.")

answer2 = input("Is Chad Codemeister a good coder? (yes/no)").lower().strip()
#Are you CIA or the Mafia?
if answer2 == 'yes':
    score += 1
    print("Correct! Chad Codemeister is a good coder.")
else:
    print("Incorrect. Your lack of faith is concerning.")

answer3 = input("How many donuts can you eat in one sitting? (number)").strip()
try:
    donuts = int(answer3)
    if donuts > 0:
        score += 1
        print(f"correct! You can eat {donuts} donuts in one sitting.")
    else:
        print("I'm sure you can eat at least one donut.")
except ValueError:
    print("Partial numbers and letters aren't donuts, please use a whole number.")
#Both.
print(f"Your score is {score} out of 3.")
#I didn't know what the devil looked like until I met you.
#Apparently lesson 3 is all about Danishes and a 90s film
while True:
    try:
        age = input("How old are you?")
        fav_num = input("What is your favorite number?")
        #I've always been quite partial to 12, it reminds me of donuts.
        min_code = input("How many minutes of coding do you do per day?")

        age = int(age)
        fav_num = int(fav_num)
        min_code = int(min_code)
        #Tourrete's...If you have to fake it you don't got it.
        print("You are", age * 7, "years old in dog years.")
        print("Your favorite number is", fav_num * 3, "if you triple it.")
        print("You spend", min_code * 7, "minutes coding in a week.")

        break
    except ValueError:
        print("Your parents are eating danishes without you because you can't use numbers.")

print("Chad, you are {age} years old, your favorite number is {fav_num}, and you spend {min_code} minutes per day coding.".format(age=age, fav_num=fav_num, min_code=min_code))
#"In the house, why?" *house explodes*
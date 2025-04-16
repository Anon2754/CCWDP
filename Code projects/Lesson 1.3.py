#I'm sailing, I'm a sailor, I sailed.
print(type("Chad Codemeister"))
#I'm guessing this tells me what type of variable that combination of characters are.
print(type(69))
#nice
print(type(69.420))
#nice, but also a decimal number
print(type(True))
#Baby steps, untie your booleans

while True:
    try:
        age = input("How old are you?")
        print(type(age))
        age = int(age)
        print(type(age))
        print(age * 7) #age in dog years
        print("You are", age * 7, "in dog years.")
        #the bags of danishes I left around your neck, where did you leave them?
        break
    except ValueError:
        print("Your numbers do not add up, now hand over the cookies.")
#HE CAN BORROW MY SLICKER

while True:
    #It's called Danish Therapy Bob, it's an instant cure
    try:
        price= float(input("What is the price of your soul?")) #a danish
        taxed_price = price * 1.69 #the nice tax
        print("The final price, with tax:", round(taxed_price, 2))
    #is this some new radical form of therapy?
        break
    except ValueError:
        print("That's not how this works, you can't just throw letters at me and expect me to know what you mean.")
#Enough to fool my staff? I don't think so.

#You think he's gone? HE'S NEVER GONE!
while True:
    try:
        meal_total = float(input("What is the total of your meal?"))
        tip = float(input("What percentage would you like to tip? (0-100)")) / 100
        tip_amount = meal_total * tip
        total = meal_total + tip_amount
        print("Your total is:", round(total, 2))
        #I'll be quiet. And I'll be peace. (laughter ensues)
        break
    except ValueError:
        print("Invalid entry, Danishes are not valid currency.")
#He let me stay in his house, he let me sleep in his bed. He let me borrow his Danish.
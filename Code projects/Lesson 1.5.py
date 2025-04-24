#Can I stay with you, please?
number = int(input("Enter a number: "))
if number > 100:
    print("Slow down, buddy, that's too high!")
elif number == 100:
    print("Good job, you picked 100!")
#So that's his castle, you think he might be compensating for something?
elif number == 69:
    print("Nice.")
else: 
    print("The number represents your self esteem, and it's low.")
#Sure it's big enough, but look at the location!


age = int(input("How old are you? "))
while True:
    has_id = input("Do you have an ID? (yes/no) ").strip().lower()
    if has_id in ["yes", "no"]:
        break
    print("Please answer with 'yes' or 'no'.")

vip = input("What is your ID number? ").strip()

while True:
    bdonut = input("Did you bring donuts? (yes/no) ").strip().lower() 
    if bdonut in ["yes", "no"]:
        break
    print("Did you bring donuts or not?")
#Ugh, it's hideous.

if age >= 18:
    if has_id == "yes":
        print("Access granted.")
        if vip == "5247":
            print("Welcome, Codemeister.")
        elif bdonut == "yes":
            print ("Thanks for the donuts!")
        else:
            print("Welcome, guest.")   
            #That's not very nice, it's just a donkey. 
    else:
        print("Sorry, no ID, no entry, babyface.")
else:
    print("Sorry, if you're not 18, then you're 12.")
#I have helmet hair.
if age >= 18 and has_id == "yes" and vip == "5247": 
    print("There are muffins and hot chocolate waiting for you, Codemeister.")
elif age >= 18 and has_id == "yes":
    print("You may now use the muffin button.")
else:
    print("Access denied, apple fritter enjoyer.")
#Cake! Everybody loves cake. Cakes have layers.

if age >= 18 and has_id == "yes" and vip == "5247":
    status = "Full Access"
elif age >= 18 and has_id == "yes":
    status = "Limited Access"
else:
    status = "No Access"
# What? It's a compliment.
if status == "Full Access":
    print("Full Access Granted.")
elif status == "Limited Access":
    print("Limited Access Granted.")
# You need a mint or something cause your breath STINKS!
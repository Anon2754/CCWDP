donut = input("What kind of donuts did you bring?").strip()
#Sugar dumplings are just giant donut holes
drink = input("What kind of drink did you bring?").strip()

print(f"So you brought {donut} and {drink} to drink.")
#Why do they even take the hole out of the donut? It makes no sense.
while True:
    try:
        age = int(input("How old are you? "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age >= 120:
            print("What are you, a vampire? Please enter a valid age.")
        else:
            print("Seems like a real number.")
            break
    except ValueError:
        print("We aren't Romans, please use real numbers.")
#Donut holes do slap though

bdonut = input("Did you bring donuts? (yes/no) ").strip().lower()
if bdonut not in ["yes", "no"]:
    print("Did you bring donuts or not?")
#cinnamon rolls are honorary donuts
has_id = input("Did you bring an ID? (yes/no) ").strip().lower()
if has_id not in ["yes", "no"]:
    print("Invalid input, please answer with a 'yes' or 'no'.")

while True:
    id_num = input("What is your ID number? ").strip()
    if id_num.isdigit() and len(id_num) == 4:
        break
    print("Invalid ID number. Please enter a 4-digit number.")
# I like my donuts with maple frosting and bacon bits
if age >= 18:
    if bdonut == "yes":
        if has_id == "yes":
            if id_num == "5247":
                print("Welcome, Codemeister. You have full access.")
            else:
                print("Welcome, guest. Thanks for the donuts! You have limited access.")
        else:
            print("I see you have donuts, but no ID. You may sit at the kids table.")
    else:
        print("No Donuts, no ID, and you want in? Sorry, we don't serve your kind here, apple fritter enjoyer.")
else:
    print("Sorry, if you're not 18, then you're 12.")

#I like my donuts soft and fluffy, though old fashioned donuts are still fantastic.
faccess = "Full Access" 
Laccess = "Limited access"
Denied = "Denied"


if has_id == "yes" and id_num == "5247" or bdonut == "yes":
    status = faccess
    print("Full access granted, welcome Codemeister!")

if has_id == "yes" and id_num not in ["5247"] and bdonut == "yes":
    status = Laccess
    print("Limited access granted, thanks for the donuts!")
#how dare you suggest apple fritters
if has_id == "yes" and id_num not in ["5247"] and bdonut == "no":
    status = Laccess
    print("Limited access Granted, but no donuts? get your act together.")

if has_id == "no":
    status = Denied
    print("Access Denied, apple fritter enjoyer.")
#The donuts will continue until morale improves

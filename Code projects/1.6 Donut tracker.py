#Your name means death
donuts = ["maple bar", "sprinkles", "apple fritter", "chocolate glazed", "old fashioned", "cake donut", "chili"]
print (donuts[0].title() + "s are the best donuts!")
donuts.append("powdered sugar")
donuts.remove("chili")
donuts.pop(2)
#FBI, you're under arrest! You have the right to remain silent. If you give up that right, you may talk, sing, dance, impersonate Elvis, or anything else you'd like.

print("What donuts would you like to have?")
for donut in donuts:
    print(f"{donut.title()}")
#in the old days we used to use zippo lighters and drain rats.
for index, donut in enumerate(donuts, start=1):
    print(f"{index}. {donut.title()}")  

interaction_cut_short = False

donut_list = []
while True:
    flavor = input("Enter a donut flavor (or 'done' to finish):").strip().lower()
    if flavor == 'done':
        break
    elif flavor == "maple bar":
        donut_list.append(flavor.title()) #Look at those Alligators, do you see them?
        print("Maple bars are the best!")
    elif flavor == "jelly filled":
        print("A person of culture, I see, unfortunately, we don't have that flavor.")
    elif flavor == "sprinkles":
        donut_list.append(flavor.title()) #you owe me $47.50 for a new stroller
        print("Homer Simpson would be proud!") 
    elif flavor == "apple fritter":
        print("What is wrong with you, those aren't donuts, get out of my shop!")
        interaction_cut_short = True
        break    
    elif flavor in donuts:
        donut_list.append(flavor.title()) #Afternoon sister, don't miss the gators.
        print(f"{flavor.title()} is a great choice!")
    else:
        print(f"Sorry, {flavor} is not a valid selection. Please try again.")
#My name... is Morty
if interaction_cut_short:
    print ("You have been banned from this donut shop for life!")
else:
    print("\nyour personalized donut lineup:")
    for d in donut_list:
        print(f"- {d.title()}")
#Muerte.
#I kill you.
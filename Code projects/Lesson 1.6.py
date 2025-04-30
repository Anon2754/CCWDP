#It was a fair fight, 2 of them, 2 of us
donuts = ["chocolate", "apple fritters", "glazed", "old fashioned", "jelly", "sprinkles", "chili"]
print(donuts[0]) 
donuts.append("powdered")
donuts.remove("apple fritters")
donuts.pop(5)
#My name.... is Muerte

for donut in donuts:
    print(f"Now serving: {donut.title()}")
#Can you say "plastic explosives"? 
for index, donut in enumerate(donuts, start=1):
    print(f"{index}. {donut.title()}")
#You know what's funny.... that grey van over there...
donut_list= []
while True:
    flavor = input("Enter a donut flavor (or 'done' to finish): ").strip().lower()
    if flavor == 'done':
        break
    elif flavor in donuts:
        donut_list.append(flavor)
    else:
        print(f"Sorry, {flavor} is not available. Please choose from the list: ")
#it's been sitting there for 7 minutes with the motor running
print("\n Your personalized donut lineup:")
for d in donut_list:
    print(f"- {d.title()}")
#Nobody looks at the driver.
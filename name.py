name = input("Please enter your name: ")
print("Hello, " + name + "! Nice to meet you.")

age = input("What is your age? ")
print("You are " + age + " years old!")

country = input ("What country are you from? ")
if country == 'USA':
    print("Wow I have heard America is very beautiful!")
if country == 'India':
    print("I love Indian food!")
else:
    print("Wow I want to visit " + country)

print("So your name is " + name + " and your age is " + age + " and you are from " + country + "?")
if input(str) == 'yes':
    print("My data is all correct then!")
if input(str) == 'no':
    print("Are you sure it is not accurate")
else: print("please enter a yes or no")

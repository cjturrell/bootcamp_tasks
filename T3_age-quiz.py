# A program that declares which age category using if, elif and else

# Ask user to input age
age = int(input("What is your age?"))

# Outputs which age category
if  age < 13:
    print("You qualify for the kiddie discount")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 100:
    print("Sorry you are dead!")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You are over the hill.")
else:
    print("Age is but a number")
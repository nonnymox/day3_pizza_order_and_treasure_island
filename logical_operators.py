height= int(input('Welcome to the rollercoaster express!\nPlease enter your height in cm: '))
bill = 0
if height > 120:
    age = int(input("Please enter your age: "))
    if age < 12:
        bill += 5
    elif age < 18:
        bill += 7
    elif age >=45 and age <= 55:
        bill += 0
    else:
        bill+= 12
    photos = input("Do you want photos? Enter Yes or no: ").lower()
    if photos == "yes":
        bill += 3
        print(f"Your total bill is ${bill}")
    elif photos == "no":
        print(f"Your total bill is ${bill}")
    else:
        print("Enter a valid input")

else:
    print("Can't ride yet, sorry!")
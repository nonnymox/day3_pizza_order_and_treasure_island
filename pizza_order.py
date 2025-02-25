print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()

bill = 0

if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("Please enter S, M, or L")
    exit()

add_pepperoni = input("Do you want pepperoni? Y or N ").lower()

if add_pepperoni == "y":
    if size == "s":
        bill += 2  # Small pizza gets $2 for pepperoni
    else:
        bill += 3  # Medium and large pizzas get $3 for pepperoni
elif add_pepperoni != "n":
    print("Please enter Y or N")
    exit()

extra_cheese = input("Do you want extra cheese? Y or N ").lower()

if extra_cheese == "y":
    bill += 1
elif extra_cheese != "n":
    print("Please enter Y or N")
    exit()

print(f"Your final bill is ${bill}")

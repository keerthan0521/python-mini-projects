# display welcome message
print("Welcome to rollercoaster ")

# ask user to input height in cm
height = float(input("what is your height in cm ? "))
new_age = int(input("what is your age ? "))

# check whether height is greater than 120cm
if height >= 120:
    if new_age >= 18:
        print("Congrats! you can ride with bill $12")
    elif new_age < 12:
        print("Congrats! you can ride with bill $5")
    else:
        print("Congrats! you can ride with bill $7")

else:
    print("Sorry! you cant ride")







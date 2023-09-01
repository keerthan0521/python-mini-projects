print("Welcome to Tip Calculator") #welcome message
bill = float(input("what was the total bill? $"))
tip = int(input("what percentage of tip would you like to give ? 10, 12 or 15 ? "))
people = int(input("How many people to split the bill ? "))
#tip_calculation_logic
new_bill = bill + (bill / tip)

pay = new_bill / people
new_pay = round(pay, 2)
print(f"Each person should pay {new_pay}") #fstring to format

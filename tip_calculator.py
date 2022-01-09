print("Welcome to the tip calculator!\nLet me ask you some questions.\n")

bill = float(input("First of all, what was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_value = bill / 100 * tip
bill_total = bill + tip_value
bill_per_person = format(bill_total / people, ".2f")

print(f"\nEach person should pay ${bill_per_person}.")

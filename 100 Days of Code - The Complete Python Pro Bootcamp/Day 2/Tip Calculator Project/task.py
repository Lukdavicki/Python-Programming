print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip/100
calculation = (bill/people)*tip_as_percent
print(f"Each of the guest have to pay {round(calculation,2)}")
#%%
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
total_children = int(input("How many children are there? "))
total_adults = int(input("How many adults are there? "))
sales_tax = float(input("What is the sales tax rate? "))
sales_tax = sales_tax/100
meal_total = child_meal*total_children+adult_meal*total_adults
tax = meal_total * sales_tax
total = meal_total + tax
tip = 0
print()
print(f"Subtotal: ${(meal_total):.2f}") # This :.2f makes sure that it will only show two decimal places.
print(f"Sales Tax: ${(tax):.2f}")
tip_bool = bool(input("Would you like to tip? (True or False) ")) # Checks if the person wants to leave a tip through a bool value
if tip_bool == True: # Checks if bool value is true
    tip_perecentage = float(input("What is your tip percentage?(0.00-1.00) ")) # This is where you enter your tip percentage
    tip = total*tip_perecentage
payment = float(input("What is the payment amount? "))
print(f"Tip: ${(tip):.2f}")
print(f"Total: ${(total+tip):.2f}")
print(f"Change: ${(payment)-(total+tip):.2f}") 
#%%
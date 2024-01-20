total = 0 
x = -1
action = 0
shopping_cart = []
price_list = []
print("Welcome to the Shopping Cart Program!")
while x < 0:
    print()
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    action = int(input("Please enter an action: "))
    if action not in [1,2,3,4,5]:
        print("invalid")
    if action == 1:
        item = input("What item would you like to add? ")
        price = float(input(f"What is the price of {item}? "))
        print(f"{item} has been added to cart.")
        shopping_cart.append(item)
        price_list.append(price)
        total = total + price
    if action == 2:
        print("Shopping Cart:")
        for i, item in enumerate(shopping_cart):
            print(f"{i + 1}. {item} - ${price_list[i]:.2f}")
    if action == 3:
        print()
    if action == 4:
        print(f"Total: ${total}")
    if action == 5:
        print("Thank you goodbye!")
        quit()

    
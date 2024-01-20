total = 0.00 
x = -1
action = 0
item_list = []
price_list = []
print("Welcome to the Shopping Cart Program!")
while True:
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
        item_list.append(item)
        price_list.append(price)
        total = total + price
    if action == 2:
        print("Shopping Cart:")
        for i, item in enumerate(item_list):
            print(f"{i + 1}. {item} - ${price_list[i]:.2f}")
    if action == 3:
        i = int(input("Which item would you like to remove? ")) - 1
        if 0 <= i < len(item_list):
            removed_item = item_list.pop(i)
            removed_price = price_list.pop(i)
            total -= removed_price
            print(f"Item {removed_item} with price ${removed_price:.2f} has been removed from the cart.")
        else:
            print("Invalid index. Please enter a valid item index.")
    if action == 4:
        print(f"The total price of the items in the shopping cart is ${total:.2f}.")
    if action == 5:
        print("Thank you goodbye!")
        quit()

    


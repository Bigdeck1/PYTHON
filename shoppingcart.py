#shopping cart

item = input("What item do you want to buy? ")
price = float(input("What is the price?: "))
quantity = int(input("How many would like to buy?: "))
total = price * quantity

print(f"You bought Item:{item} quantity: {quantity}/s")
print(f"Your total is: {total}")

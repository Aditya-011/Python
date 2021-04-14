price_item1 = float(input('Enter price of item 1: '))
quantity_item1 = int(input("Enter quantity of item 1: "))
price_item2 = float(input('Enter price of item 2: '))
quantity_item2 = int(input("Enter quantity of item 2: "))
price_item3 = float(input('Enter price of item 3: '))
quantity_item3 = int(input("Enter quantity of item 3: "))
price_item4 = float(input('Enter price of item 4: '))
quantity_item4 = int(input("Enter quantity of item 4: "))

total_item1 = price_item1*quantity_item1
total_item2 = price_item2*quantity_item2
total_item3 = price_item3*quantity_item3
total_item4 = price_item4*quantity_item4

total_price = total_item1+total_item2+total_item3+total_item4

print("Your total price is ", str(total_price))

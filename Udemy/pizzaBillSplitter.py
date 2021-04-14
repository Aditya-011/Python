user_1 = str(input("Enter name of User 1: "))
user_2 = str(input("Enter name of User 2: "))
user_3 = str(input("Enter name of User 3: "))
user_4 = str(input("Enter name of User 4: "))

pizza_price = float(input('Enter total price of pizza: '))
total_slices = int(input('Enter total slices in pizza: '))

slices_user1 = int(input('Enter slices ' + user_1 + ' had: '))
slices_user2 = int(input('Enter slices ' + user_2 + ' had: '))
slices_user3 = int(input('Enter slices ' + user_3 + ' had: '))
slices_user4 = int(input('Enter slices ' + user_4 + ' had: '))

amt_user1 = slices_user1 / total_slices * pizza_price
amt_user2 = slices_user2 / total_slices * pizza_price
amt_user3 = slices_user3 / total_slices * pizza_price
amt_user4 = slices_user4 / total_slices * pizza_price

print("Amount to be paid by "+user_1 + ": " + str(amt_user1))
print("Amount to be paid by "+user_2 + ": " + str(amt_user2))
print("Amount to be paid by "+user_3 + ": " + str(amt_user3))
print("Amount to be paid by "+user_4 + ": " + str(amt_user4))

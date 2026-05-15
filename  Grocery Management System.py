'''
This application allows you to shop things based on their entire cost and add 
Ontario tax. The program will read the item names and prices from the [items] 
file and store them in a list. In addition, the user can add more things 
and their pricing; this is completely optional. Also, the program has an offer
that if the user spend $55, they will receive a 10% discount. 
After calculation, the user will receive a receipt with information about 
the total cost, discount, tax, and subtotal.
'''

#Opens the file [items] to read
file = open("Items.txt", "r")

#Storing the items in a list
items= []

#Reading the file
for line in file:
    line = line.strip() #to remove spaces or lines
    parts = line.split(",") # to split into item and price

    name = parts[0] 
    price = float(parts[1]) #to convert int to float

    items.append((name, price)) #using tuple to store variable names
    
file.close()

#After reading file
#the user can add more items
answer = input("Do you want to add more items? yes/no: ")

while answer == "yes":
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))

    items.append((name, price)) #Storing the new items

    answer = input("Add another item? yes/no: ")

#Ontario tax calculated
def calculate_tax(subtotal):
    return subtotal * 0.13 #This adds the Ont tax

subtotal = 0 #to count the total

#looping the items to calculate total price
for item in items:
    name = item[0] #get the item name
    price = item[1] #get the price=
    subtotal += price #adding price for each item

#Applying discount 10% on 55$
if subtotal >= 55: #Checking if the total qualifies 55$
    discount = subtotal * 0.10
    print("You got a 10% discount!")
else: #if it doesn't qualify then we keep discount 0
    discount = 0
    print("No discount applied")

#Calculate tax and final total
tax = calculate_tax(subtotal) # using the function to calculate subtotal
final_total = subtotal + tax - discount

#Outputting the Reciepts
print("\n--- Receipt ---")
print("Total: $", round(subtotal, 2))
print("Discount: -$", round(discount, 2))
print("Tax: $", round(tax, 2))
print("Final total: $", round(final_total, 2))
#Importing random function
import random

#Menu for the restaurant stored in nasted list
menu = [["Fried Rice", 140], 
        ["Masala Tea", 20], 
        ["Cheese Burger", 80], 
        ["Chicken Pizza", 450], 
        ["Soft Drinks", 40]]

#An empty list is created to append the values into the list
orders = []

#This function generates a unique random variable everytime a new order is created
def generateUniqueId():
    #declared a varible and initilised its value to 0
    random_number = 0
    #a for loop will iterate over 0 - 9 five times
    for i in range(5):
        digit = random.randint(0, 9)  
        random_number = random_number * 10 + digit
    return random_number

#This fuction will create new order, it will show menu, ask quatity and then append the details into the empty list
def createNewOrder():
    order_id = generateUniqueId()
    items_ordered = []
    
    print("Menu:")
    #Diplsy the menu on the screen
    for i, (item, price) in enumerate(menu, start=1):
        print(f"{i}. {item} - Rs{price}")
    
    #a while loop will start for user to keep entring their order untill the user input 0
    while True:
        item_number = int(input("Enter your choice): "))
        if item_number == 0:
            break
        #this basically give a constraint on item_number
        elif item_number < 1 or item_number > len(menu):
            print("Invalid Option selection!!")
            continue
        
        quantity = int(input("Enter quantity: "))
        #this basically give a constraint on quantity
        if quantity < 1:
            print("Not available. Please enter a quantity greater than 0.")
            continue
        
        items_ordered.append({"itemnumber": item_number, "quantity": quantity})
    
    order = {"Orderid": order_id, "items": items_ordered}
    orders.append(order)
    print(f"Order {order_id} created successfully!")

#This function will allow the user to view their order by displaying it on the screen
def viewYourOrderDetails():
    for order in orders:
        order_id = order["Orderid"]
        items_ordered = order["items"]
        total_price = 0
        
        print(f"Order {order_id}:")
        for item in items_ordered:
            item_number = item["itemnumber"]
            quantity = item["quantity"]
            item_name, item_price = menu[item_number - 1]
            subtotal = item_price * quantity
            total_price += subtotal
            print(f"{item_name} x{quantity}: ${subtotal}")
        
        print(f"Total: Rs{total_price}")
        print()

#Main code, to implement all the functions we have created above
while True:
    print("Menu:")
    print("1. Create new order")
    print("2. View Orders")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    #for options on the screen
    if choice == "1":
        createNewOrder()
    elif choice == "2":
        viewYourOrderDetails()
    elif choice == "3":
        with open("23122033_shubhamKumar.txt", "w") as file:
            for order in orders:
                file.write(str(order) + "\n")
        print("Orders saved to '23122033_shubhamKumar.txt'.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")

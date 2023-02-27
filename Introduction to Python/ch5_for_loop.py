# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program acts as a cashier terminal, prompting for the number of items and
# then asking for the description, price and quantity. It displays a subtotal for
# each item as well as a running final total

# Import the cashier_calculation file so that we can use the item_calculation function
# Set total to 0 as a starting number
# Determine how many times we will loop the program
# Loops the program based on user in put for times
# Prompts for the description
# Prompts for the price
# Prompts for the quantity
# Uses the item_calculation function to print and return the subtotal 
# Keep a running grand total
# Display the final grand total
# Call the main function only if the file is being run as
# a stand alone program  


# Import the cashier_calculation file so that we can use the item_calculation function
import cashier_calculation

def main():
    # Set total to 0 as a starting number
    total = 0
    # Determine how many times we will loop the program
    times = int(input("How many items are being purchased? "))

    # Loops the program based on user in put for times
    for num in range(times):
        # Prompts for the description
        description = input(f"Enter description of item {num+1} ")
        # Prompts for the price
        price = float(input(f"Enter the price of item {num+1} "))
        # Prompts for the quantity
        quantity = float(input(f"Enter the quantity of item {num+1} "))
        # Uses the item_calculation function to print and return the subtotal 
        subtotal = cashier_calculation.item_calculation(description, price, quantity)
        # Keep a running grand total
        total = subtotal + total

    # Display the final grand total
    print(f"\nYour total is ${total:,.2f}")
    
# Call the main function only if the file is being run as
# a stand alone program  
if __name__ == '__main__':
    main()

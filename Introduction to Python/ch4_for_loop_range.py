# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program gets an item, price and quantity and calculates a total three times, then giving a grand total
# Set the grand total amount to start
# Create a for loop that repeats three times
# Get the item name
# Get the item quantity
# Calculate the total
# Calculate the running total
# Display the quantity, item, price and total to be looped 3 times
# Display the grand total   

def main():
    # Set the grand total amount to start
    grand_total = 0
    # Create a for loop that repeats three times
    for point_of_sale in range(3):
        # Get the item name
        item = input('Enter item name ')
        # Get the item price
        price = float(input(f'Enter unit price of {item} '))
        # Get the item quantity
        quantity = float(input(f'Enter quantity of {item} '))
        # Calculate the total
        total = price * quantity
        # Calculate the running total
        grand_total = grand_total + total
        # Display the quantity, item, price and total to be looped 3 times
        print(f"{quantity:,.0f} {item} @ ${price:,.2f}, total ${total:,.2f}")
    # Display the grand total    
    print(f"Total of these three items is ${grand_total:,.2f}")
   
main()

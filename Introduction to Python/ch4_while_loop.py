# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program prints tax and a subtotal for amounts under $5 in 20 cent increments. 
# Display headers. Centered and spaced by 9
# Input constant
# Start the amount for the loop
# create a loop that continues up to 5
# Calculate tax
# Calculate the total
# print the amount, tax and total. Centered, columned and 9 wide
# Add .2 for next loop

def main():

    # Display headers. Centered and spaced by 9
    print(f"{'SUBTOTAL':^9}{'SALES TAX':^9}{'TOTAL':^9}")
    print(f"{'--------':^9}{'---------':^9}{'-----':^9}")

    # Input constant
    SALES_TAX = .07
    # Start the amount for the loop
    amount = 0.2

    # create a loop that continues up to 5
    while amount < 5.1:
        # Calculate tax
        tax = amount * SALES_TAX
        # Calculate the total
        total = amount + tax
        # print the amount, tax and total. Centered, columned and 9 wide
        print(f"{amount:^9.2f}{tax:^9.2f}{total:^9.2f}")
        # Add .2 for next loop
        amount += .2


   
main()

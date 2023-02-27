# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# Open betterbuy_sale.txt and assign to sale_data
# Display the top line of the table. Items at 20 spaces and the rest at 15 per column
# Read the first line and assign to name
# Create a while loop that continues to read lines in threes until complete
# Strip \n from the name line
# Read the second line and assign to regular_price as a float
# Read the third line and assign to reduction as a float
# Divide reduction by 100 to be able to use as a percent
# Find reduced amount by multiplying the reduction percent and regular price
# Find the sale price by subtracting the reduced amount by the regular price
# Display in column form the name of the item, the regular price, the reduced amount and the 
# sale price. First column is 15 spaces and 15 for the rest
# Start the loop over by reading the next line (or quit of none)
# Close the file when complete
# Call the main function only if the file is being run as
# a stand alone program  




def main():

    # Open betterbuy_sale.txt and assign to sale_data
    sale_data = open('betterbuy_sale.txt', 'r')

    # Display the top line of the table. Items at 20 spaces and the rest at 15 per column
    print(f"{'ITEM':<20}{'REG.PRICE':>15}{'REDUCED':>15}{'SALE PRICE':>15}")

    # Read the first line and assign to name
    name = sale_data.readline()

    # Create a while loop that continues to read lines in threes until complete
    while name != '':
        # Strip \n from the name line
        name = name.rstrip('\n')
        # Read the second line and assign to regular_price as a float
        regular_price = float(sale_data.readline())
        # Read the third line and assign to reduction as a float
        reduction = float(sale_data.readline())
        # Divide reduction by 100 to be able to use as a percent
        reduction_percent = reduction / 100
        # Find reduced amount by multiplying the reduction percent and regular price
        reduced = reduction_percent * regular_price
        # Find the sale price by subtracting the reduced amount by the regular price
        sale_price = regular_price - reduced
        # Display in column form the name of the item, the regular price, the reduced amount and the 
        # sale price. First column is 15 spaces and 15 for the rest
        print(f"{name:<20}{regular_price:>15,.2f}{reduced:>15,.2f}{sale_price:>15,.2f}")
        # Start the loop over by reading the next line (or quit of none)
        name = sale_data.readline()


    # Close the file when complete
    sale_data.close()   



    
# Call the main function only if the file is being run as
# a stand alone program  
if __name__ == '__main__':
    main()

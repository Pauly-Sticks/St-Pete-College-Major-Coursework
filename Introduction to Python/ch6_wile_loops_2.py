# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# Associate sale_data with opening betterbuy_sale.txt in write mode
# Ask user for the item name
# create a while loop ending with enter
# Ask user for the regular price. Convert to string
# Ask user for the reduction percentage. Convert to string
# Write the name to sale_data
# Write the regular_price to sale_data
# Write the reduction to sale_data
# Continue the loop or end with enter
# When complete, display end message
# Close the file
# Call the main function only if the file is being run as
# a stand alone program  




def main():

    # Associate sale_data with opening betterbuy_sale.txt in write mode
    sale_data = open('betterbuy_sale.txt', 'w')

    # Ask user for the item name
    name = input("Enter item name or Enter to Quit ")

    # create a while loop ending with enter
    while name != "":
       
        # Ask user for the regular price. Convert to string
        regular_price = str(input("Enter item's regular price "))
        # Ask user for the reduction percentage. Convert to string
        reduction = str(input("Enter reduction percent for the sale "))
        # Write the name to sale_data
        sale_data.write(name + '\n')
        # Write the regular_price to sale_data
        sale_data.write(regular_price + '\n')
        # Write the reduction to sale_data
        sale_data.write(reduction + '\n')

    
        # Continue the loop or end with enter
        name = input("Enter item name or Enter to Quit ")
    
    # When complete, display end message
    print('File was created')

    # Close the file
    sale_data.close()



    
# Call the main function only if the file is being run as
# a stand alone program  
if __name__ == '__main__':
    main()

# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610
# Note - I saw in one of the videos how it is best to break things way down and keep it as simple as possible.
#   In this program, I used one print function for the entire output to show that I know page breaks and how to
#   start one line of code on a new line. If not for this, I probably would have gone with three different print
#   lines. I am including the code to match the output being flush to the left in a note below. Thanks!

# Display title
# Get item's unit_price from the user
# Get the quantity from the user
# Get the TAX_RATE constant
# Calculate the subtotal
# Calculate the tax
# Calculate the total_due
# Display the subtotal, sales tax and total due

def main():
    # Title
    print('Sales tax tool')
    # Get the unit_price. Note the \' for the apostrophe
    unit_price = float(input('What is the item\'s unit price? $'))
    # Get the quantity
    quantity = int(input('What is the quantity? '))
    # Get the SALES_TAX
    TAX_RATE = 0.07
    # Get the subtotal
    subtotal = unit_price * quantity
    # Get the tax
    tax_due = TAX_RATE * subtotal
    #Get the total_due
    total_due = tax_due + subtotal
    # Display the subtotal, sales tax and total due. Note \n's for new lines and \'s to break up lines
    print(f'{quantity:.0f} units at ${unit_price:,.2f} equals a subtotal of ${subtotal:,.2f}.\n\
    The sales tax is ${tax_due:,.2f}.\n\
    The total due is ${total_due:,.2f}.')

    # Alternate print lines that would show outputs flush to the left. 3 lines. Does not show proficiency in page breaks
    # print(f'{quantity:.0f} units at ${unit_price:,.2f} equals a subtotal of ${subtotal:,.2f}.')
    # print(f'The sales tax is ${tax_due:,.2f}.')
    # print(f'The total due is ${total_due:,.2f}.')

main()

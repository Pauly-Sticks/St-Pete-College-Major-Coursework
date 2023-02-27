# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# Display title line
# Get miles
# Get MILES_TO_KILO constant
# Calculate kilometers
# Display miles and the converted kilometers




def main():
    # Title line
    print('Miles to Kilometers conversion calculator')
    # Getting the user to input miles
    miles = float(input('Input the number of miles: '))
    # Inputting the constant
    MILES_TO_KILO = (1.60934)
    # Calculate the Kilometers
    kilo = miles*MILES_TO_KILO
    # Display the results
    print(f'{miles:,.2f} miles is equal to {kilo:,.3f} kilometers. Safe travels!')

main()

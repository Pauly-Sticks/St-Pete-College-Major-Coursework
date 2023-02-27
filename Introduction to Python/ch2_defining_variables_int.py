# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610
# Note - I stuck with how to do this with just the info in Ch2 (versus using the fraction command). Hope I
#   didnt miss anything.

# Display the title
# Get the numerator from the user
# Get the denominator from the user
# Calculate the integer
# Calculate the remaining numerator
# Display the mixed number by printing the integer and the remaining numerator with / denominator


def main():
    # Program title
    print('Improper fraction to mixed number converter')
    # Get the numerator
    numerator = int(input('Input the Numerator: '))
    # Get the denominator
    denominator = int(input('Input the Denominator: '))
    # Calculate the integer
    whole_number = numerator//denominator
    # Calculate the remaining numerator
    remaining_numerator = numerator % denominator
    # Display the mixed number
    print(f'{numerator}\\{denominator} is equal to {whole_number} {remaining_numerator}\\{denominator}')

main()

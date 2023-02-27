# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This is a program that asks for a two digit integer, if acceptable, then asks for a different two digit integer, 
# which then determines which one was greater and by how much. Both inputs must be acceptable.

# Prompt user for a two digit integer
# Calculate if input_1 complies. must be > 9 and < 100
    # If correct, have the user enter another two digit integer
    # Calculate if input_2 complies. must be >, < 100 and not equal to input_1
        # If the second number complies, we need to see if input_1 is larger than input_2
            # Calculate difference_a
            # Display that input_1 is greater than input_2 by difference_a. 
        # If the second number complies and input_2 is greater than input_1
            # Calculate the difference
            # Display that input_2 is greater than input_1 by difference_b.
    # Display that something is wrong with the second input
# Display that something is wrong with the first input

def main():
    # Prompt user for a two digit integer
    input_1 = int(input('Enter a two-digit integer '))
    # Calculate if input_1 complies. must be > 9 and < 100
    if input_1 > 9 and input_1 < 100:
        # If correct, have the user enter another two digit integer
        input_2 = int(input('Enter another DIFFERENT two-digit integer '))
        # Calculate if input_2 complies. must be >, < 100 and not equal to input_1
        if input_2 > 9 and input_2 < 100 and input_1 != input_2:
            # If the second number complies, we need to see if input_1 is larger than input_2
            if input_1 > input_2:
                # Calculate difference_a
                difference_a = input_1 - input_2
                # Display that input_1 is greater than input_2 by difference_a. 
                print(f'{input_1:d} is larger than {input_2:d} by {difference_a:d}')
            # If the second number complies and input_2 is greater than input_1
            else:
                # Calculate the difference
                difference_b = input_2 - input_1
                # Display that input_2 is greater than input_1 by difference_b.
                print(f'{input_2:d} is larger than {input_1:d} by {difference_b:d}')
        # Display that something is wrong with the second input
        else:
            print('Something is wrong with the second input. Try again.') 
    # Display that something is wrong with the first input
    else:
        print('Something is wrong with the first input. Try again.')
   
main()



# Below is a more complex solution that includes a reply if the user uses a decimal
#def main():
    # Prompt user for a two digit integer
    #input_1 = float(input('Enter a two-digit integer '))
    # Calculate the integer of input_1
    #input_1_int = input_1 // 1
    # Calculate if input_1 complies. must be > 9, < 100 and it must = input_1_int to make sure it is an int and not decimals
    #if input_1 > 9 and input_1 < 100 and input_1 == input_1_int:
        # If correct, have the user enter another two digit integer
        #input_2 = float(input('Enter another DIFFERENT two-digit integer '))
        # Calculate the integer of input_2
        #input_2_int = input_2 // 1
        # Calculate if input_2 complies. must be > 9, < 100 and it must = input_2_int to make sure it is an int and not decimals
        #if input_2 > 9 and input_2 < 100 and input_1 != input_2 and input_2 == input_2_int:
            # If the second number complies, we need to see if input_1 is larger than input_2
            #if input_1 > input_2:
                # Calculate difference_a
                #difference_a = input_1 - input_2
                # Display that input_1 is greater than input_2 by difference_a. Make sure numbers look like integers and not floats
                #print(f'{input_1:.0f} is larger than {input_2:.0f} by {difference_a:.0f}')
            # If the second number complies and input_2 is greater than input_1
            #else:
                # Calculate the difference
                #difference_b = input_2 - input_1
                # Display that input_2 is greater than input_1 by difference_b. Make sure numbers look like integers and not floats
                #print(f'{input_2:.0f} is larger than {input_1:.0f} by {difference_b:.0f}')
        # Display that something is wrong with the second input
        #else:
            #print('Something is wrong with the second input. Try again.') 
    # Display that something is wrong with the first input
    #else:
        #print('Something is wrong with the first input. Try again.')
   
#main()


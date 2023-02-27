# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program tells the user if a number is or is not an odd multiple of 19 that is more than 60 and 
# less than 200.

# Get user_input as "Enter a multiple of 19 that is more than 60 and less than 200"
# Calculate result. user_input must be < 200, > 60, divisible by 19 ( % 19 == 0) and odd ( % 2 == 1).
# If the input does not match the parameters, display Bad Attempt


def main():
    
    # Get user_input as "Enter a multiple of 19 that is more than 60 and less than 200"
    user_input = int(input('Enter a multiple of 19 that is more than 60 and less than 200: '))
    # Calculate result. user_input must be < 200, > 60, divisible by 19 ( % 19 == 0) and odd ( % 2 == 1).
    if user_input > 60 and user_input < 200 and user_input % 19 == 0 and user_input % 2 == 1:
        print(f"{user_input} is a good input")
    # If the input does not match the parameters, display Bad Attempt
    else:
        print('Bad Input')

   
main()

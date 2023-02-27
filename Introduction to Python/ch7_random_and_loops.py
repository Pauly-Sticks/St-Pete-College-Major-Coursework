# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program compiles, sorts and lists temperatures

# Get 50 random numbers assigned to celsius
# Display the lowest and the highest numbers obtained
# Determine if 0 is in the list. If so, display the position. If not, display that fact
# Get a subset of 10 unique numbers from celsius
# Sort the new list ascending
# Display that ten numbers were sorted
# equate fahrenheit with a function that pulls in the celsius subset
# Get how many items are in the fahrenheit list
# Display the celsius and fahrenheit headings
# Create a loop that displays each number in the celsius subset and fahrenheit in 
# column form
# Start an accumulator to add values in celsius subset
# Accumulate celsius totals
# Average the celsius totals
# Start an accumulator to add values to fahrenheit
# Accumulate fahrenheit totals
# Average the fahrenheit totals
# Print space
# Print both averages
# Create a function that converts celsius to fahrenheit
# Return the list to fahrenheit
# Call the main function only if the file is being run as
# a stand alone program  

# import random module 
import random

def main():

    # Get 50 random numbers assigned to celsius
    celsius = [random.randint(-40,40) for x in range(50)]

    # Display the lowest and the highest numbers obtained
    print(f"Lowest temp is {min(celsius)}C and highest is {max(celsius)}C")

    # Determine if 0 is in the list. If so, display the position. If not, display that fact
    if 0 in celsius:
        print(f"Found 0C in index {celsius.index(0)}")
    else:
        print ("0C was not recorded")

    # Get a subset of 10 unique numbers from celsius
    celsius_subset = random.sample(celsius, k=10)

    # Sort the new list ascending
    celsius_subset.sort()

    # Display that ten numbers were sorted
    print("Sorted sample of ten equivalent temperatures")

    # equate fahrenheit with a function that pulls in the celsius subset
    fahrenheit = f_to_c(celsius_subset)

    # Get how many items are in the fahrenheit list
    temp_nums = len(fahrenheit)

    # Display the celsius and fahrenheit headings
    print(f"{'CELSIUS':<10}{'FAHRENHEIT':<12}")

    # Create a loop that displays each number in the celsius subset and fahrenheit in 
    # column form
    for y in range(temp_nums):
        print(f"{celsius_subset[y]:^7}{fahrenheit[y]:^13,.1f}")

    # Start an accumulator to add values in celsius subset
    c_total = 0

   # Accumulate celsius totals
    for c_add in celsius_subset:
        c_total += c_add

    # Average the celsius totals
    c_avg = c_total / temp_nums

    # Start an accumulator to add values to fahrenheit
    f_total = 0

    # Accumulate fahrenheit totals
    for f_add in fahrenheit:
        f_total += f_add
    
    # Average the fahrenheit totals
    f_avg = f_total / temp_nums

    # Print space
    print("")

    # Print both averages
    print(f"{c_avg:^7.1f}{f_avg:^13.1f}{'<--- averages':^15}")

# Create a function that converts celsius to fahrenheit
def f_to_c(celsius_subset):
    fah = [9/5 * x + 32 for x in celsius_subset]
    # Return the list to fahrenheit
    return fah

# Call the main function only if the file is being run as
# a stand alone program  
if __name__ == '__main__':
    main()

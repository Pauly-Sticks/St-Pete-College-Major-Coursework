# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program uses nested loops to start with 0123456789 and work down to 0
# Create a for loop that starts at 10 and works down to 1
# Input num as 0 to reset the num value after the loop or else it will keep counting
# Create a loop for each line that starts at 0 and counts up by one per the number of iterations left via r
# Advance the line

def main():

    # Create a for loop that starts at 10 and works down to 1
    for r in range(10,0,-1):
        # Input num as 0 to reset the num value after the loop or else it will keep counting
        num = 0
        # Create a loop for each line that starts at 0 and counts up by one per the number of iterations left via r
        for c in range(r):
            print(num, end="")
            num += 1
        # Advance the line
        print()

main()

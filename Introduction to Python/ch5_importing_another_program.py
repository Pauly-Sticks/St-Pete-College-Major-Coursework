# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program prompts for the radius of a circle and then displays
# the area and circumference

# Import the program5_2 file so that we can use the return_the_area and print_the_circumference
# functions
# Get the radius from the user
# Call the return_to_area function from program5_2 then area
# Display the area
# Call the print_the_circumference function from program5_2 and then circumference
# Call the main function only if the file is being run as
# a stand alone program  


# Import the program5_2 file so that we can use the return_the_area and print_the_circumference
# functions
import program5_2

def main():

    # Get the radius from the user
    radius = float(input("Enter radius of circle "))
    # Call the return_to_area function from program5_2 then area
    area_calc = program5_2.area.return_the_area(radius)
    # Display the area
    print(f"The area of a circle with radius {radius:,.1f} is {area_calc:,.4f}")
    # Call the print_the_circumference function from program5_2 and then circumference
    program5_2.circumference.print_the_circumference(radius)



    
# Call the main function only if the file is being run as
# a stand alone program  
if __name__ == '__main__':
    main()

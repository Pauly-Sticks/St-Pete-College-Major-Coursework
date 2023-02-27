# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# This program prompts for the radius of a circle and then displays
# the area and circumference


# Import the circumference file to use the print_the_circumference function
# Import the area file to use the return_the_area function
# Get the radius from the user
# Call the return_to_area function
# Display the area
# Call the print_the_circumference function. 
# Call the main function only if the file is being run as
# a stand alone program  


# Import the circumference file to use the print_the_circumference function
import circumference
# Import the area file to use the return_the_area function
import area

def main():

    # Get the radius from the user
    radius = float(input("Enter radius of circle "))
    # Call the return_to_area function
    area_calc = area.return_the_area(radius)
    # Display the area
    print(f"The area of a circle with radius {radius:,.1f} is {area_calc:,.4f}")
    # Call the print_the_circumference function. 
    circumference.print_the_circumference(radius)



    
# Call the main function only if the file is being run as
# a stand alone program  
if __name__ == '__main__':
    main()

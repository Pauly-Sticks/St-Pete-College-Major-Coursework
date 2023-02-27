# SPC ID#2437441
# Paul Stickrath - OFR_COP1000_1464_0610

# Create blank dictionary
# Get course code
# Create a loop that ends with enter
# Get grade
# assign key and value to the dictionary
# Restart the loop
# Set starting values for grade total, number of courses and the lowest score
# Create a loop to print the courses and grades
# Keep a running total of the grade amounts
# Calculate the grade average
# Keep track of the lowest score and save the data for later
# Display the average score
# Display the lowest course and score
# Display that we dropped the lowest class and remove from the dictionary
# Display that we will be showing the revised grades
# Reset the running total for grades
# Display the subject and grades
# Keep track of the grades running total
# Keep an average of the grade scores
# Display the final average
# Call the main function only if the file is being run as
# a stand alone program  


def main():

    # Create blank dictionary
    course_dict = {}

    # Get course code
    course = input(f"Input course code or Enter to quit ")

    # Create a loop that ends with enter
    while course != "":
        # Get grade
        grade = int(input(f"Grade in {course} as % "))

        # assign key and value to the dictionary
        course_dict[course] = grade

        # Restart the loop
        course = input(f"Input course code or Enter to quit ")

    # Set starting values for grade total, number of courses and the lowest score
    total_grades = 0
    num_of_courses = 0
    lowest_score = 100

    # Create a loop to print the courses and grades
    for k in course_dict:
        print(f"Grade in {k} is {course_dict[k]}%")

        # Keep a running total of the grade amounts
        total_grades += course_dict[k]
        # Calculate the grade average
        avg_score = total_grades/len(course_dict)
        # Keep track of the lowest score and save the data for later
        if course_dict[k] < lowest_score:    
            lowest_score = course_dict[k]
            lowest_class = k

    # Display the average score
    print(f"Current term average is {avg_score:.1f}%")
    # Display the lowest course and score
    print(f"Worst course is {lowest_class} : {lowest_score}%")

    # Display that we dropped the lowest class and remove from the dictionary
    print(f"Dropped {lowest_class}")
    del course_dict[lowest_class]

    # Display that we will be showing the revised grades
    print(f"Here are my revised grades...")

    # Reset the running total for grades
    total_grades = 0

    # Display the subject and grades
    for k,v in course_dict.items():
        print(f"Grade in {k} is {v}%")
        # Keep track of the grades running total
        total_grades += v
        # Keep an average of the grade scores
        avg_score = total_grades/len(course_dict)

    # Display the final average
    print(f"Revised term average is {avg_score:.1f}%")
  
# Call the main function only if the file is being run as
# a stand alone program  
if __name__ == '__main__':
    main()

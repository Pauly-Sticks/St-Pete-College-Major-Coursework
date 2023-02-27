/*
    Ask user for three numbers. If any side is longer than the other two combined, 
    return you cannot make a triangle. 

*/

const readlineSync = require('readline-sync');

let again = 'y';

// Use a while loop to determine if the user wants to continue
while (again == 'y' || again == 'Y' || again == 'yes' || again == 'Yes' || again == 'YES') {
    console.log("Lets calculate if your three measurements can create a valid triangle. Input the length of each of the three sides.")
    const choiceOne = parseInt(readlineSync.question('Enter the length of the first side :'));
    const choiceTwo = parseInt(readlineSync.question('Enter the length of the second side :'));
    const choiceThree = parseInt(readlineSync.question('Enter the length of the final side :'));

    // Use an if statement to see if any two sides do not add up to the third
    if ((choiceOne + choiceTwo < choiceThree) || (choiceOne + choiceThree < choiceTwo) || choiceTwo + choiceThree < choiceOne) {
        // Assign the choices to an array and then identify the smallest and largest so that we may suggest a proper third choice if the triangle is not valid
        const choices = [choiceOne, choiceTwo, choiceThree];
        smallestChoice = Math.min(...choices);
        largestChoice = Math.max(...choices);
        // Display if a triangle cannot be made. Suggest increasing the smallest choice
        console.log('You cannot make a triangle with these measurements of ' + choiceOne + ', '+ choiceTwo + ' and ' + choiceThree + '.' );
        console.log('Your smallest choice was ' + smallestChoice + ' while your largest choice was ' + largestChoice + '. Your third choice would need to be at least ' + (largestChoice - smallestChoice) + ' in order for the triangle to be valid');
     } else {
        // Display if a triangle can be made. 
        console.log('With these measurements of of ' + choiceOne + ', '+ choiceTwo + ' and ' + choiceThree + ', you can form a valid triangle.')
    }
    again = readlineSync.question('Would you like to try again? ');
}

console.log('Program Closing');


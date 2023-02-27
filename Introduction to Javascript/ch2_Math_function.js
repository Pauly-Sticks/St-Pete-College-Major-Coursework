/*
    This program estimates the square root of a number to .0001 using a while loop and not
    a Math.sqrt.
*/



const readlineSync = require('readline-sync');

let again = 'y';

// Uses a while loop to determine if the user wants to continue
while (again == 'y' || again == 'Y' || again == 'yes' || again == 'Yes' || again == 'YES') {
    // Gets user input for a and n
    console.log("This program will estimate the square root of a decimal number of your choosing.")
    const n = parseInt(readlineSync.question('Enter an number (can be a decimal) for n: '));

    // Creates the first set of estimates. One using the x0 = (x0 + (a/x0))/2 and the other just 
    // taking n/2
    estimateOne = (((n/2) + (n/(n/2)))/2);
    estimateTwo = n;
    // Calculates the difference between the two
    difference = Math.abs(estimateOne-estimateTwo);

    // Plug the last result into the equation and then calculates the difference between the new
    // and the last. Takes the difference and makes it its positive version so that we can test for
    // distance between the two in absolute values. Loops until difference is less than .0001.
    while (difference > 0.0001) {
        estimateTwo = ((estimateOne + (n/estimateOne))/2);
        difference = Math.abs(estimateOne-estimateTwo);
        estimateOne = estimateTwo;
    }

    // Display results
    console.log("The approximate square root of " + n + " is " + estimateTwo);

    // Ask if user would like to try again
    again = readlineSync.question('Would you like to try again? ');
}

//Exit message
console.log("Program closing");
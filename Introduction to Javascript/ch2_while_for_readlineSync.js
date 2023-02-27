/*
    This program uses a loop vs Math.pow to calculate thr result of a chosen number and a power.
*/


const readlineSync = require('readline-sync');

let again = 'y';

// Use a while loop to determine if the user wants to continue
while (again == 'y' || again == 'Y' || again == 'yes' || again == 'Yes' || again == 'YES') {
    // Get user input for a and n
    console.log("This is an exponent calculator to calculate a number (a) raised to the nth(n) power.")
    const a = parseInt(readlineSync.question('Enter a number for a: '));
    const n = parseInt(readlineSync.question('Enter a number for n: '));

    // Assign a to total to start
    total = a;

    // create a loop to add a to itself n times. Make sure that i starts at 1 so that math is accurate. 
    for (i = 1; i < n; i++) {
        total = total * a
    }

    // Display results
    console.log(a + " to the " + n + " power is " + total);

    // Ask if user would like to try again
    again = readlineSync.question('Would you like to try again? ');
}

//Exit message
console.log("Program Closing");
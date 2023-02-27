/*
    This program will prompt a user to enter 10 integers. These integers will be
    placed in array. The program will then reverse the order of the numbers by
    swapping array locations. 
*/



const readlineSync = require('readline-sync');

let again = 'y';

// Create an empty array
let userInput = new Array(10);

let n = userInput.length

// Use a while loop to determine if the user wants to continue
while (again == 'y' || again == 'Y' || again == 'yes' || again == 'Yes' || again == 'YES') {


    // Prompt user for 10 integers
    console.log("This program will enter 10 numbers of your choosing into an array")
    console.log("It will reverse them and display the new array.")
    questionUserForIntegers();

    // Swap the integers from the lowest array address to the highest and continue
    // back. Made sure to stop the loop at n/2 before the program continued to 
    // swap integers back to original.
    for (i = 0; i < n/2; i++) {
        t = userInput[i];
        userInput[i] = userInput[n - (i + 1)];
        userInput[n - (i + 1)] = t;
    }

    console.log("Reversing order... *beep* *boop* *beep* *boop*")

    // Display the new order of the array
    for (i = 0; i < n; i++) {
        console.log("The number is array " + i + " is now " + userInput[i]);
    }

    // Ask if user would like to try again
    again = readlineSync.question('Would you like to try again? ');
}

// Exit message
console.log("Program Closing");

function questionUserForIntegers() {
    userInput[0] = parseInt(readlineSync.question('Enter integer number one: '));
    userInput[1] = parseInt(readlineSync.question('Enter integer number two: '));
    userInput[2] = parseInt(readlineSync.question('Enter integer number three: '));
    userInput[3] = parseInt(readlineSync.question('Enter integer number four: '));
    userInput[4] = parseInt(readlineSync.question('Enter integer number five: '));
    userInput[5] = parseInt(readlineSync.question('Enter integer number six: '));
    userInput[6] = parseInt(readlineSync.question('Enter integer number seven: '));
    userInput[7] = parseInt(readlineSync.question('Enter integer number eight: '));
    userInput[8] = parseInt(readlineSync.question('Enter integer number nine: '));
    userInput[9] = parseInt(readlineSync.question('Enter integer number ten: '));
}

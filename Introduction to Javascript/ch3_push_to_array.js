/*
    This program take numbers that the user inputs and then sorts them low to high
    and then removes all duplicates. It then shortens the array so that it is only the size
    of the new set.
*/

const readlineSync = require('readline-sync');

// Create an empty array
let userArray = new Array();

let i = 0

// User instructions
console.log("This program will take numbers that you input and remove duplicates.")
console.log("Enter a negative number when done with input.")

userInput = 1

// Use a while loop to continue as long as the numbers are positive
while (userInput >= 0) {
    // Get user input
    userInput = parseInt(readlineSync.question('Please enter a number to add to the array: '));
    // Push the users input into the array
    userArray.push(userInput);
    i++;
}

// Remove the last negative input
userArray.splice(userArray.length-1, 1);

// Sort the array low to high
userArray.sort(function(a, b){return a - b});

let uniqueElements = 0

// Use a for loop to continue while i is less than the userArray length
for (let i = 1; i < userArray.length; i++) {
    // Use a while loop to see if array[i] is not equal to the array at the position of the
    // unique elements. If not equal, unique element count +1 and the new unique element
    // position has the array[i] moved in
    while ((userArray[i]) != (userArray[uniqueElements])) {
        uniqueElements++;
        userArray[uniqueElements] = userArray[i];
    }
}

// reduce the size of the array by having the total elements equal the unique elements +1
userArray.length = uniqueElements + 1;

// Display the results
console.log("Your new array in order and without duplicates is:");
console.log(userArray);

// Exit message
console.log("Program Closing")
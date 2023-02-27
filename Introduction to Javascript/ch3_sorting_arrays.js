/*
    This program asks the user for how many duplicates they want in their array. It then asks the user for nubmer inputs and then sorts them low to high
    and then removes the duplicates until there is an acceptable level. 
*/

const readlineSync = require('readline-sync');

// Create an empty array
let userArray = new Array();

let i = 0

// User instructions
console.log("This program will take numbers that you input and remove duplicates.")
console.log("Enter a negative number when done with input.")
// Prompt user to determine how many duplicates are acceptable.
duplicatesAllowed = parseInt(readlineSync.question('How many duplicates will you allow?: '));

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

// Display the sorted results so that we can compare to the final results
console.log("Your new sorted array is: ");
console.log(userArray);

// Use a for loop to continue while i is less than the userArray length
for (let i = 0; i < userArray.length; i++) {

    // use indexOf and LastIndexOf to determine the first and last positions of a particular number
    let firstInstance = userArray.indexOf(userArray[i]);
    let lastInstance = userArray.lastIndexOf(userArray[i]);
    let numOfDuplicates = lastInstance - firstInstance;
    let elemToEliminate = numOfDuplicates - duplicatesAllowed + 1;

    // Use the difference of the last and first positions as well as the duplicates allowed to determine how many instances
    // we need to remove from the array. Starting from the first instance, remove the desired number of duplicates to match
    // the users desired maximum
    if ((lastInstance - firstInstance) >= duplicatesAllowed) {
        userArray.splice((firstInstance), (elemToEliminate));
    } 
}

// Display the results
console.log("Your new array in order and with no more than " + duplicatesAllowed + " duplicates is:");
console.log(userArray);

// Exit message
console.log("Program Closing")
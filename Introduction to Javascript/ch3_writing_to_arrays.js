/*

    This program allows the user to input as many grades as they need. The program then 
    displays how many students scored a particular grade through a histogram. 

*/ 

const readlineSync = require('readline-sync');

// Create an empty array
let scores = new Array(101).fill(0);

let n = scores.length

let grade = 1

console.log("This program create a histogram based on the grades that you input")
console.log("A grade of 0 will exit the input phase")

// Use a while loop to determine if the user wants to continue
while (grade > 0) {
    // Get user input
    grade = parseInt(readlineSync.question('Please enter a grade: '));
    // Assign a 1 to the score[grade] array that they chose
    scores[grade] = scores[grade] + 1;
    // Tell the user that the score has been recorded. Uses an IF statement so that if the user inputs 0, then no 
    // message will display
    if (grade > 0) {
    console.log("You entered a score of " + grade + ". " + scores[grade] + " student(s) received this grade.");
    }
}

console.log("");
console.log("The following is a histogram of your scores: ")

// Loop through each part of the array and repeat a "*" for each 1 in the array.
for ( i = 1; i < n; i++) {
    if (scores[i] > 0) {
        console.log(i + ": " + "*".repeat(scores[i]));
    }
}

// Exit message
console.log("End of histogram");
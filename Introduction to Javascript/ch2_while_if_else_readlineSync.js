/*
    Fermat's Last Theorem states that there are no integers a, b and c such that
    a^n + b^n = c^n except when n<=2. The user will enter a, b, c and n and 
    the program will show if Fermat's Theorem holds true. 
*/




const readlineSync = require('readline-sync');

let again = 'y';

// Use a while loop to determine if the user wants to continue
while (again == 'y' || again == 'Y' || again == 'yes' || again == 'Yes' || again == 'YES') {

    // Get a, b, c and n from user
    console.log("Lets calculate if Fermat's Last Theorem holds true.")
    const a = parseInt(readlineSync.question('Enter an integer for a: '));
    const b = parseInt(readlineSync.question('Enter an integer for b: '));
    const c = parseInt(readlineSync.question('Enter an integer for c: '));
    const n = parseInt(readlineSync.question('Enter an integer for n: '));

    // Calculate a, b and c to the nth power
    aToNth = Math.pow(a, n);
    bToNth = Math.pow(b, n);
    cToNth = Math.pow(c, n);
    
    // Display if Fermat's Theorem does not hold
    if ( n >= 2 && ((aToNth + bToNth) == cToNth)) {
        console.log(a + ' to the ' + n + ' power is ' + aToNth + '.');
        console.log(b + ' to the ' + n + ' power is ' + bToNth + '.');
        console.log(c + ' to the ' + n + ' power is ' + cToNth + '.');
        console.log(aToNth + " plus " + bToNth + ' equals ' + cToNth + "! Fermat's Theorem does not hold!")
    // Display if Fermat's Theorem holds
     } else {
        console.log(a + ' to the ' + n + ' power is ' + aToNth + '.');
        console.log(b + ' to the ' + n + ' power is ' + bToNth + '.');
        console.log(c + ' to the ' + n + ' power is ' + cToNth + '.');
        console.log(aToNth + " plus " + bToNth + ' equals ' + (aToNth + bToNth) + '. This does not equal ' + cToNth + ". Fermat's Theorem holds.")
    }
    // Ask if user would like to try again
    again = readlineSync.question('Would you like to try again? ');
}

// Exit message
console.log("Program Closing");

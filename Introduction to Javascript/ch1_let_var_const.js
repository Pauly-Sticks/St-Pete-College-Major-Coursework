/* 
    Program: Displaying the number of seconds since midnight, seconds remaining in the day, % of time that has passed and then the total 
            time that it has taken to write this program.

    Input: Approximated time in hours, minutes and seconds.
            Constants for seconds in a minute, hour and day
 */

// Setting the current time when I started the program
let hour = 9;
let minute = 29;
let second = 41;

// Setting constants that we will use to calculate time below
const SECONDSINAMINUTE = 60;
const SECONDSINANHOUR = SECONDSINAMINUTE * 60;
const HOURSINADAY = 24;
const SECONDSINADAY = HOURSINADAY * SECONDSINANHOUR;

// Calculating how many seconds have passed since midnight and then displaying them.
let secondsSinceMidnight = (hour * SECONDSINANHOUR) + (minute * SECONDSINAMINUTE) + second;
console.log("The amount of seconds that have passed since midnight is " + secondsSinceMidnight + " total seconds.\n");

// Calculating the remaining seconds in the day and then displaying them
let remainingSeconds = SECONDSINADAY - secondsSinceMidnight;
console.log("The amount of seconds remaining in the day is " + remainingSeconds + " seconds.\n") ;

// Calculating the percentage of time that has passed in the day and then displaying them.
let percentagePassed = (secondsSinceMidnight / SECONDSINADAY) * 100;
percentagePassed = percentagePassed.toFixed(2);
console.log("The percentage of the day that has passed is " + percentagePassed + "%.\n");

// Getting a current Date so that we can calculate the time from the start of the program to now. Did not calculate for year, month and day so this is only relative
// to the time of the day that one runs the program. 
let nowLater = new Date();
let hourLater = nowLater.getHours();
let minuteLater = nowLater.getMinutes();
let secondLater = nowLater.getSeconds();

// Determine difference from current time and input time above
let newSecondsSinceMidnight = (hourLater * SECONDSINANHOUR) + (minuteLater * SECONDSINAMINUTE) + secondLater;

// Break down the difference in seconds to its hours, minutes and seconds using the Math.floor function and getting the remainders
let totalSecondsElapsed = newSecondsSinceMidnight - secondsSinceMidnight;
let hoursElapsed = Math.floor(totalSecondsElapsed/SECONDSINANHOUR);
let minutesElapsed = Math.floor((totalSecondsElapsed%SECONDSINANHOUR)/SECONDSINAMINUTE);
let secondsElapsed = totalSecondsElapsed - (hoursElapsed * SECONDSINANHOUR) - (minutesElapsed * SECONDSINAMINUTE);

// Display the time diference between now and the input time at the start of the program
console.log("The time that has elapsed since I started programing this program has been " + hoursElapsed + " hours, " + minutesElapsed + " minutes and " + secondsElapsed + " seconds.");












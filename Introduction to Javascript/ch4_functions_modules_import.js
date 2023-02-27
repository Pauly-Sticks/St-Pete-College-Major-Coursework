/*
    This program uses various functions loaded from conversionUtils.js to convert one length into another
*/ 

// Load in the modules
const utils = require("./ch4_functions_modules_export")


const readlineSync = require('readline-sync');

console.log("This program will allow you to convert various lengths.");

// Prompts user to select a conversion to make
selection = chooseAConversion();

// While loop for menu selection
while (selection != 9) {

    if (selection == 1) {
        console.log('Ok, lets convert centimeters to millimeters...');
        centimeters = parseFloat(readlineSync.question('Please enter the number of centimeters: '));
        answer = utils.centi_to_milli(centimeters).toFixed(3);
        console.log(centimeters + " centimeters is equivilant to " + answer + " millimeters.")

    } else if (selection == 2) {
        console.log('Ok, lets convert meters to centimeters...');
        meters = parseFloat(readlineSync.question('Please enter the number of meters: '));
        answer = utils.meter_to_centi(meters).toFixed(3);
        console.log(meters + " meters is equivilant to " + answer + " centimeters.")

    } else if (selection == 3) {
        console.log('Ok, lets convert kilometers to meters...');
        kilometers = parseFloat(readlineSync.question('Please enter the number of kilometers: '));
        answer = utils.kilo_to_meter(kilometers).toFixed(3);;
        console.log(kilometers + " kilometers is equivilant to " + answer + " meters.")

    } else if (selection == 4) {
        console.log('Ok, lets convert inches to centimeters...');
        inches = parseFloat(readlineSync.question('Please enter the number of inches: '));
        answer = utils.inch_to_centi(inches).toFixed(3);;
        console.log(inches + " inches is equivilant to " + answer + " centimeters.")

    } else if (selection == 5) {
        console.log('Ok, lets convert feet to centimeters...');
        feet = parseFloat(readlineSync.question('Please enter the number of feet: '));
        answer = utils.feet_to_centi(feet).toFixed(3);;
        console.log(feet + " feet is equivilant to " + answer + " centimeters.")

    } else if (selection == 6) {
        console.log('Ok, lets convert yards to meters...');
        yards = parseFloat(readlineSync.question('Please enter the number of yards: '));
        answer = utils.yard_to_meter(yards).toFixed(3);;
        console.log(yards + " yards is equivilant to " + answer + " meters.")

    } else if (selection == 7) {
        console.log('Ok, lets convert miles to meters...');
        miles = parseFloat(readlineSync.question('Please enter the number of miles: '));
        answer = utils.mile_to_meter(miles).toFixed(3);;
        console.log(miles + " miles is equivilant to " + answer + " meters.")

    } else if (selection == 8) {

        console.log('Ok, lets convert miles to kilometers...');
        miles = parseFloat(readlineSync.question('Please enter the number of miles: '));
        answer = utils.mile_to_kilo(miles);
        console.log(miles + " miles is equivilant to " + answer + " kilometers.")

    } else {
        console.log("You did not make a valid choice, please try again...");
    }

    console.log("");
    console.log("");
    selection = chooseAConversion();

}

console.log("Thank you for using the length converter!");

// Prompts user to select a conversion to make
function chooseAConversion() {
    console.log("Please make a selection:");
    console.log("To convert centimeters to millimeters, type 1:");
    console.log("To convert meters to centimeters, type 2:");
    console.log("To convert kilometers to meters, type 3:");
    console.log("To convert inches to centimeters, type 4:");
    console.log("To convert feet to centimeters, type 5:");
    console.log("To convert yards to meters, type 6:");
    console.log("To convert miles to meters, type 7:");
    console.log("To convert miles to kilometers, type 8:");
    console.log("To Exit, type 9:");
    userSelection = parseFloat(readlineSync.question('Please make your selection: '));
    console.log("")
    return userSelection
}
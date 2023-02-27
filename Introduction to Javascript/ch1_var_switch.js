/* 
    Program: This program creates variables named day, date, month and year.
            day = day of the week (Friday)
            month = Month of the year (January)
            date needs to be a format like the 13th using a number. 

    Input: Date()

    Process: We will be able to just assign year and date from the getFullYear and getDate
            functions. For month and day, we will need to use switch so that we can assign
            the getMonth and getDay from numbers to a string output like Thursday or 
            February

    Output: American format:
            Thursday, July 16, 2022
            European format:
            Thursday 16 July 2022


 */

let now = new Date();
year = now.getFullYear();
date = now.getDate();

switch (now.getMonth()) {
    case 0:
        month = "January";
       break;
    case 1:
        month = "February";
       break;
    case 2:
        month = "March";
       break;
    case 3:
        month = "April";
       break;
    case 4:
        month = "May";
       break;
    case 5:
        month = "June";
       break;
    case 6:
        month = "July";
       break;
    case 7:
        month = "August";
       break;
    case 8:
        month = "September";
       break;
    case 9:
        month = "October";
       break;
    case 10:
        month = "November";
       break;
    case 11:
        month = "December";
       break;
}

switch (now.getDay()) {
    case 0:
        day = "Sunday";
       break;
    case 1:
        day = "Monday";
       break;
    case 2:
        day = "Tuesday";
       break;
    case 3:
        day = "Wednesday";
       break;
    case 4:
        day = "Thursday";
       break;
    case 5:
        day = "Friday";
       break;
    case 6:
        day = "Saturday";
       break;
}
// Code below for testing
//console.log(day);
//console.log(month);
//console.log(date);
//console.log(year);

console.log("American format:");
console.log(day + ", " + month + " " + date + ", " + year);
console.log("European format:");
console.log(day + " " + date + " " + month + " " + year);
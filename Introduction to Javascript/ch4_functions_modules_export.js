/*
    A program of functions made to be used as modules for other programs.
    Each converts a length from one type to another
*/

function centi_to_milli(centimeter) {

    return centimeter * 10;
}

function meter_to_centi(meter) {

    return meter * 100;
}

function kilo_to_meter(kilo) {

    return kilo * 1000;
}

function inch_to_centi(inch) {

    return inch * 2.54;
}

function feet_to_centi(feet) {

    return feet * 30.48;
}

function yard_to_meter(yard) {

    return yard * .9144;
}

function mile_to_meter(mile) {

    return mile * 1609.34;
}

function mile_to_kilo(mile) {

    return mile * 1.60934;
}


// Export the functions above
module.exports = {
    centi_to_milli,
    meter_to_centi,
    kilo_to_meter,
    inch_to_centi,
    feet_to_centi,
    yard_to_meter,
    mile_to_meter,
    mile_to_kilo,
}
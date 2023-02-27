
// Slideshow
var images = ['images/heroImage_2400x1800.jpg','images/coffee_2400x1800.jpg','images/street_2400x1800.jpg'];

let smallImages = ['images/heroImage_768w.jpg','images/coffee_768w.jpg','images/street_768w.jpg'];

var i =0;


function slideShow() {

    document.getElementById("image").src=images[i];



    //document.getElementsByClassName(".top-image img").style.animation="fadeIn 2s";

    if(i<images.length-1){
        i++;
    } else {
        i=0;
    }

    setTimeout("slideShow()" , 5000);
}

function smallSlideShow() {

    document.getElementById("image").src=smallImages[i];


    //document.getElementsByClassName(".top-image img").style.animation="fadeIn 2s";

    if(i<images.length-1){
        i++;
    } else {
        i=0;
    }

    setTimeout("slideShow()" , 5000);
}


if (window.innerWidth > 760) {
    window.onload = slideShow;
} else {
    window.onload = smallSlideShow;
}

// Navigation Menu Hamburger

const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.nav-menu');

menu.addEventListener('click', function(){
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
})




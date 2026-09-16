


//selecting elements

let ham = document.querySelector('.ham');
let navbar = document.querySelector('nav ul');
//on click ham should toogle

//if ham is clicked, check if navbar has a class of hide_bar, if it has it, remove the class but if it does not change the ham bar, hide one of them and make the other to slant on top of each other using css translate 
ham.addEventListener('click', function(){
    navbar.classList.toggle('hide_navbar');

})
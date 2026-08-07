// HOME PAGE ENGINE START

// SIDE BAR START
const btn = document.getElementById("cart-add");
const sidebar = document.getElementById("sidebar");
let index = 0;

if (btn && sidebar) {

btn.addEventListener("click", function(){

    if(index == 0){
        sidebar.style.transform = `translateX(0)`;
        index = 1;
    }
    else{
        sidebar.style.transform = `translateX(100%)`;
        index = 0;
    }

});

}


// MENU ICON FOR PHONE

let manue1 = document.getElementById('manue1');
let navbtn = document.getElementById('navbtn');
let login = document.querySelectorAll('.login');
let x = document.getElementById('x');


if(manue1 && navbtn && x){

manue1.addEventListener("click", ()=>{

    x.style.display = 'block';

    navbtn.style.display = 'grid';
    navbtn.style.backgroundColor = '#666';
    navbtn.style.position = 'absolute';
    navbtn.style.top = '60px';
    navbtn.style.width = '70%';
    navbtn.style.padding = '10px';
    navbtn.style.right = '0px';

});


x.addEventListener('click', ()=>{

    x.style.display = 'none';
    navbtn.style.display = 'none';

    login.forEach(item => {
        item.style.display = "none";
    });

});

}

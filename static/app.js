// HOME PAGE ENGER START
// 1 SIDE BARE START
const btn = document.getElementById("cart-add");
const sidebar = document.getElementById("sidebar");
let index = 0;

btn.addEventListener("click", function(){

if(index == 0){
sidebar.style.transform=`translateX(0)`
index=1;
}
else{
    sidebar.style.transform=`translateX(100%)`
index=0;
}

});
const pres = document.querySelector('#pres')
// 1 SIDE BARE e

fetch('/api/product/1/')
    .then(response => response.json())
    .then(data => {
        console.log(data.qut);
    })
    .catch(error => {
        console.error(error);
    });

    //  This is a menue icon for Phone 

let manue1  = document.getElementById('manue1');
let navbtn = document.getElementById('navbtn');
let login = document.querySelectorAll('.login');
let x = document.getElementById('x')

manue1.addEventListener("click", ()=>{

    
    x.style.display = 'block'
    navbtn.style.display = 'block';
    navbtn.style.display = 'grid';
    navbtn.style.backgroundColor = ' #666';
    navbtn.style.position = 'absolute';
    navbtn.style.top = '60px';
    navbtn.style.width = '70%';
    navbtn.style.padding = '10px';
    navbtn.style.position = 'absolute';
    // navbtn.style.overflow = 'hidden';

    navbtn.style.right = '0px'

//     login.forEach(item => {
//     item.style.display = "block";
// });
    
})

x.addEventListener('click', ()=>{
    
     x.style.display = 'none'
      navbtn.style.display = 'none';
      login.forEach(item => {
    item.style.display = "none";
});
})





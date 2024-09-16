// Navigation

const nav = document.querySelector(".main-nav");
const btnHamburger = document.querySelector(".hamburger-btn");
const ligneUnique =document.querySelector(".ligneUnique")


btnHamburger.addEventListener("click", toggleNav)

function toggleNav(){
    nav.classList.toggle("active");
    // if(ligneUnique.style.background.includes("rgba(255,255,255,0)")){
    //     btnHamburger.ariaExpanded = true;
    // }
    // else{
    //     btnHamburger.ariaExpanded = false;
    // }
  
}

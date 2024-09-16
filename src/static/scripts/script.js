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


// Slideshow

const slideshowImages = document.querySelectorAll(".slideshow-images-container .slide-view");
const fadeSlideDots = document.querySelectorAll(".fade-slide-dots .dot");

fadeSlideDots.forEach(dot => dot.addEventListener("click", fadeSlideshow))

let currentFadeIndex = 1;
let fadeIntervalID;

function fadeSlideshow(e){

  slideshowImages[currentFadeIndex - 1].classList.remove("active");
  fadeSlideDots[currentFadeIndex - 1].classList.remove("active");
  fadeSlideDots[currentFadeIndex - 1].ariaDisabled = "false";

  if(e) {
    currentFadeIndex = e.target.getAttribute("data-fadeIndex");
    clearInterval(fadeIntervalID)
    fadeIntervalID = window.setInterval(fadeSlideshow, 3500)
  }
  else {
    currentFadeIndex++;
    if(currentFadeIndex > slideshowImages.length) {
      currentFadeIndex = 1;
    }
  }

  slideshowImages[currentFadeIndex - 1].classList.add("active");
  fadeSlideDots[currentFadeIndex - 1].classList.add("active");
  fadeSlideDots[currentFadeIndex - 1].ariaDisabled = "true";

}

fadeIntervalID = window.setInterval(fadeSlideshow, 3500)

// levé de soleil

const sun = document.querySelectorAll("#about .reel-slide .sun");
const reelText = document.querySelectorAll("#about .reel-slide .reel-text");

let currentIndex;

reelText.forEach(dot => dot.addEventListener("mouseenter", sunrise));
reelText.forEach(dot => dot.addEventListener("mouseleave", sunset));

// reelText.addEventListener("mouseenter",()=>{
//   sun.classList.add("sunrise")
// });

function sunrise(e){
  if(e){
    currentIndex = e.target.getAttribute("index");
    sun[currentIndex-1].classList.add("sunrise");
  }
};

function sunset(e){
  if(e){
    currentIndex = e.target.getAttribute("index");
    sun[currentIndex-1].classList.remove("sunrise");
  }    
};



// commentaire

const iconComment = document.querySelector("#chat-alt-3");
const formComment = document.querySelector(".comment-container form");

iconComment.addEventListener("click", toggleComment)

function toggleComment(){
  formComment.classList.toggle("active-comment");
}




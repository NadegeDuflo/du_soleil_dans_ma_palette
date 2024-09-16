// commentaire

const iconComment = document.querySelector("#chat-alt-3");
const formComment = document.querySelector(".comment-container form");

iconComment.addEventListener("click", toggleComment)

function toggleComment(){
  formComment.classList.toggle("active-comment");
}

// USER NAME DISPLAY + PROFILE ALERT

document.addEventListener("DOMContentLoaded", function(){

let user = localStorage.getItem("loggedUser")

let userBtn = document.getElementById("userBtn")

if(userBtn && user){

userBtn.innerHTML = "👤 " + user

userBtn.onclick = function(){

alert("🚧 Profile section is under development.\nWorking in progress.")

}

}

})

// LOGOUT FUNCTION

function logout(){

localStorage.removeItem("loggedUser")

window.location.href = "index.html"

}
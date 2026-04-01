function startApp(){

document.getElementById("hero").style.display="none"
document.getElementById("app").style.display="block"

}

async function analyze(){

let file=document.getElementById("resume").files[0]
let jd=document.getElementById("jd").value

let formData=new FormData()
formData.append("file",file)
formData.append("job_description",jd)

document.getElementById("result").innerHTML="Analyzing..."

let response=await fetch("http://127.0.0.1:8000/analyze",{
method:"POST",
body:formData
})

let data=await response.json()

let analysis = data.analysis
let questions = data.questions

window.questions = questions

let score = analysis.alignment_score

if(score <= 1){
score = Math.round(score * 100)
}
else{
score = Math.round(score)
}

// let html = `


// <h3 style="margin-top:40px;">🤖 AI Interview Questions</h3>

// <button onclick="showQuestionTypes()" class="generate-btn">
// Generate Questions
// </button>

// <div id="questionTypes" style="display:none;margin-top:20px;">

// <button onclick="loadQuestions('technical')" class="qbtn">
// Technical Questions
// </button>

// <button onclick="loadQuestions('behavioral')" class="qbtn">
// Behavioral Questions
// </button>

// <button onclick="loadQuestions('scenario')" class="qbtn">
// Scenario Questions
// </button>

// </div>

// <div id="questionsOutput" class="card" style="margin-top:20px;"></div>

// `
/* store results */

let resultsData = {
score: score,
analysis: analysis,
questions: questions
}

localStorage.setItem("analysisResults", JSON.stringify(resultsData))

/* open results page */

window.location.href = "results.html"

}



/* LOGIN MODAL FUNCTIONS */

function openLogin(){
document.getElementById("loginModal").style.display="flex"
}

function closeLogin(){
document.getElementById("loginModal").style.display="none"
}

function openSignup(){
document.getElementById("signupModal").style.display="flex"
}

function closeSignup(){
document.getElementById("signupModal").style.display="none"
}

function switchToLogin(){
closeSignup()
openLogin()
}

function switchToSignup(){
closeLogin()
openSignup()
}

let generatedOTP;

function sendOTP(){

let name = document.getElementById("loginName").value
let phone = document.getElementById("phone").value;

phone = phone.replace(/\D/g,'')

if(phone.length !== 10){
alert("Enter valid mobile number");
return;
}

let storedUser = JSON.parse(localStorage.getItem("user"))

if(!storedUser){
alert("Please sign up first")
return
}

if(name !== storedUser.name || phone !== storedUser.phone){
alert("Name or phone number not registered")
return
}

/* Generate random OTP */

generatedOTP = Math.floor(100000 + Math.random() * 900000);

alert("Demo OTP: " + generatedOTP);

/* Show OTP input */

document.getElementById("phoneSection").style.display="none";
document.getElementById("otpSection").style.display="block";

}

function verifyOTP(){

let enteredOTP = document.getElementById("otp").value;

if(enteredOTP == generatedOTP){

let name = document.getElementById("loginName").value
localStorage.setItem("loggedUser", name)

alert("Login Successful ✅ Redirecting...");

/* store login status */
localStorage.setItem("loggedIn", "true")

/* redirect */
window.location.href = "analyzer.html"

}
else{

alert("Invalid OTP ❌")

}

}

function signupUser(){

let name = document.getElementById("signupName").value
let phone = document.getElementById("signupPhone").value

phone = phone.replace(/\D/g,'')

if(phone.length !== 10){

alert("Enter a valid 10 digit mobile number")
return

}

/* save user in localStorage */

let user = {
name: name,
phone: phone
}
localStorage.setItem("user", JSON.stringify(user))

let message = document.getElementById("signupMessage")

message.innerHTML = "✅ Successfully Signed Up!"

setTimeout(function(){

message.innerHTML = ""
closeSignup()
openLogin()

},2000)

}

// logout

function logout(){

localStorage.removeItem("loggedIn")

window.location.href = "index.html"

}

let user = localStorage.getItem("loggedUser")

if(user){
document.getElementById("userBtn").innerHTML = "👤 " + user
}
let randomNum=Math.round((Math.random()*100)+1);
console.log(randomNum);
const submit=document.querySelector('#subt')
const UserInput=document.querySelector('#guessField')
const guessSlot=document.querySelector('.guesses')
const remaining=document.querySelector('.lastResult')
const lowOrHi=document.querySelector('.lowOrHi')
const startOver=document.querySelector('.result')
const p=document.createElement('p')
let prevGuess=[]
let NumGuess=1
let playGame=true
if (playGame) {
 submit.addEventListener('click',function (e) {
   e.preventDefault();
   const guess=parseInt(UserInput.value);
//    console.log(guess);
      validateGuess(guess)
 })  

}
function validateGuess(guess) {
  if (isNaN(guess)) {
    alert('please enter valid number')
  }else if(guess<1){
    alert('please enter number between 1-100')
  }
  else if(guess>100){
    alert('please enter number between 1-100')
  }
  else{
    prevGuess.push(guess)
    if(NumGuess>=10){
        displayGuess(guess)
        displayMessage(`Game Over. Random Number was ${randomNum}`);
        endGame()
    }else{
        displayGuess(guess)
        checkGuess(guess)
    }
  }
}
function checkGuess(guess) {
    if(guess===randomNum)
    {
        displayMessage(`Guessed it Right, Number is ${randomNum}`)
        endGame()
    }else if(guess<randomNum){
    displayMessage(`Random Number is Higher than this`)
    }
    else if(guess>randomNum)
    {
        displayMessage(`Random Number is Lower than this`)

    }
    
}
function displayGuess(guess) {
    UserInput.value=''
    guessSlot.innerHTML+=` ${guess}`
    remaining.innerHTML=`${10-NumGuess}`
    NumGuess++;
}
function displayMessage(message) {
      lowOrHi.innerHTML=`<h2>${message}</h2>`;
}
function endGame() {
    UserInput.value=''
    UserInput.setAttribute('disabled','')
    p.classList.add('button')
    p.innerHTML=`<h2 id=newGame>Start New Game</h2>`
    startOver.appendChild(p)
    playGame=false
    newGame();

}
function newGame() {
  const newGameButton=  document.querySelector('#newGame')
   newGameButton.addEventListener('click',function(e){
    randomNum=Math.round((Math.random()*100)+1);
    prevGuess=[]
    NumGuess=1
    guessSlot.innerHTML=''
    remaining.innerHTML=`${11-NumGuess}`
    UserInput.removeAttribute('disabled')
    startOver.removeChild(p)
    displayMessage('')
    playGame=true
}) 
}
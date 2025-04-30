const randColor=function () {
    const hex='123456789ABCDEF';
    let color='#'
    for (let i = 0; i < 6; i++) {
        color+=hex[Math.floor(Math.random()*16)]   
    }
    return color
}
let interval;
const StartChangingColor=function () {
    if(!interval){
    interval= setInterval(() => {
       document.body.style.backgroundColor=randColor() 
    }, 1000);    
}}
const StopChangingColor=function () {
    clearInterval(interval)
    interval=null //to free memory after work done
}
document.querySelector('#start').addEventListener('click',StartChangingColor)
document.querySelector('#stop').addEventListener('click',StopChangingColor)


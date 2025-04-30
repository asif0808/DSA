const PromiseOne=new Promise(function (resolve,reject) {
    setTimeout(function () {
     console.log("Async task1");
     resolve()
    },1000)
})
PromiseOne.then(function(){
    console.log("promise consumed");
    
})
// another way
new Promise(function(resolve,reject){
   setTimeout(function(){
    console.log('Async task2');
    resolve()
   },1000)
    
}).then(function () {
    console.log('promise two consumed');
})
const PromiseThree=new Promise(function(resolve,reject){
   setTimeout(function(){
    resolve({username:'aasif',email:'a@a.com'})
   },1000)
})
PromiseThree.then(function(obj){
    console.log(obj);
    
})
const PromiseFour=new Promise(function(resolve,reject){
    setTimeout(function(){
        const error=false //check for true
        if(!error){
        resolve({username:"aasif",password:'a45372a'})
        }
        else{
            reject("Error, something went wrong")
        }
    },1000)
})
PromiseFour
.then((obj)=>{
    console.log(obj);
    return obj.username
}).then((usern)=>{
  console.log(usern);
}).catch((err)=>{
    console.log(err);
}).finally(()=>{
    console.log('promise is executed, either resolved or rejected');
    
})
const PromiseFive=new Promise(function(resolve,reject){
    setTimeout(function(){
        const error=true //check for false
        if(!error){
        resolve({username:"JavaScript",password:'Js5372a'})
        }
        else{
            reject("Error, something went wrong")
        }
    },1000)
})
async function ConsumePromFive() {
   try {
    const response=await PromiseFive
    console.log(response);
   } catch (error) {
    console.log(error);
   } 
    
}
ConsumePromFive()
// async function getUsers() {
//             try {
//                 const response=await fetch('https://jsonplaceholder.typicode.com/users') 
//                 console.log(typeof response);
//                 const data=await response.json()
//                 console.log(typeof data);
//                 console.log(data);
                
                
//             } catch (error) {
//                 console.log(error);
                
//             }
//  }
//  getUsers()
console.log('hello'); //executed first because of setTimeOut
//fetching the above using fetch/then
// fetch('https://jsonplaceholder.typicode.com/users')
// .then((response)=>{
//    return response.json()
// })
// .then((res)=>{
//     console.log(res);
// })
// .catch((error)=>{
//     console.log(error);
    
// })
fetch('https://api.github.com/users/asif0808')
.then((response)=>{
   return response.json()
})
.then((res)=>{
    console.log(res);
})
.catch((error)=>{
    console.log(error);
    
})
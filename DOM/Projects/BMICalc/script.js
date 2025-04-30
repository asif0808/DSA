const form=document.querySelector('form')
// thise use case will give empty values
// const height=parseInt(document.querySelector('#height').value)

form.addEventListener('submit',function(e)
{
    e.preventDefault()
   const weight=parseInt(document.querySelector('#weight').value)
   const height=parseInt(document.querySelector('#height').value)
   const results=document.querySelector('#results')
   let bmi;
   if(weight===''|| weight<0||isNaN(weight))
    {
     results.innerHTML=`${weight} Please give valid Weight`
    }
   else if(height===''|| height<0||isNaN(height))
   {
    results.innerHTML=`${height} Please give valid Height`
   }
   else{
     bmi=(weight/((height*height)/10000)).toFixed(2)
    // showing result
    results.innerHTML=`<span>${bmi}</span>`
   }

//    printing additional information
   if(bmi<18.6)
   {
    results.innerHTML=`<span>${bmi} <br> You are Underweight</span>`
   }
   else if(18.6<bmi<24.9)
   {
    results.innerHTML=`<span>${bmi} <br> You are in Normal Range</span>`
   }
   else{
        results.innerHTML=`<span>${bmi} <br> You are Overweight</span>`
       }

   


})
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
function App() {
  let [counter,setCounter]=useState(10)
  const incre=()=>{
    if (counter>=20){
      alert('Maximum Limit')
    }
    else{
    setCounter(counter+1)
  }}
  const decre=()=>{
    if (counter<=0){
      alert('Minimum Limit')
    }
    else{
    setCounter(counter-1)
  }}
  return (
    <>
      <h1>Counter With React Project</h1>
      <h2>Count : {counter}</h2>
      <button onClick={incre}>Increment </button><br/>
      <button onClick={decre}>Decrement</button>
    </>
  )
}

export default App

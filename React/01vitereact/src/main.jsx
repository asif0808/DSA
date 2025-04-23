import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import Hello from './Hello.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* multiple elements at a time can be returned */}
    <App/>
    <Hello/>
  </StrictMode>,
)

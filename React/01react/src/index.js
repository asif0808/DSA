import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import Hello from './Hello';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // return only one element after removing   <StrictMode>
<>
    <Hello/>
    <App/>
</>
);



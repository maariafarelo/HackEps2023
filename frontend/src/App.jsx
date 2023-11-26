



import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';



function App() {

  return (
  
    
    <div className='croqueta'>
      
      <div className='submitfeedback' >
        <h1> Submit your feedback! </h1> 
     </div>

     <div className='whoareyou' >
        <h3> Who are you?  </h3>
     </div>
    
     <div className='input1' >
     <input name="input1" />
      </div>

     <div className='producte' >
       <h3> Which product do you want to tell us about?</h3>
     </div>

     <div className='input1' >
      <input name="input1" />
      </div>


     <div className='proposal' >
       <h3> Explain your proposal</h3>
    </div>

    <div className='input2' >
     <input name="input2" />
      </div>

    
  
     <div className='button'>
     <button> SUBMIT </button>
     </div>
     
    

    </div>
  )
}

export default App


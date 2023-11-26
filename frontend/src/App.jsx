import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
  const [showToast, setShowToast] = useState(false);

  const handleSubmit = () => {
    const client = document.getElementsByName('input1')[0].value;
    const product = document.querySelector('.selectInput').value; // Use querySelector for select
    const feedback = document.getElementsByName('input3')[0].value;

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://127.0.0.1:5000/feedback');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
      client,
      product,
      feedback
    }));

    // Call to backend
    setShowToast(true);
  };

  return (
    <div className='mainPage'>
      <div className='submitfeedback'>
        <h1>Submit your feedback!</h1>
      </div>
      <form>
        <div className='whoareyou'>
          <h3> Which client do you represent? </h3>
        </div>
        <div className='input1'>
          <input name="input1" />
        </div>
        <div className='producte'>
          <h3> Which product do you want to tell us about?</h3>
        </div>
        <div className='input1'>
          <select className='selectInput'>
            <option name="intech3d">Intech3D</option>
            <option name="invelon">Invelon</option>
            <option name="origen">Origen</option>
            <option name="innitia">Innitia</option>
            <option name="xrshop">XRShop</option>
            <option name="ingamevr">InGameVR</option>
            <option name="print&go">Print&Go</option>
            <option name="aurora">Aurora</option>
            <option name="fabrex">Fabrex</option>
          </select>
        </div>
        <div className='proposal'>
          <h3> Explain your feedback or request</h3>
        </div>
        <div className='input3'>
          <input name="input3" />
        </div>
      </form>
      <div className='button'>
        <button onClick={handleSubmit}>SUBMIT</button>
      </div>
      {showToast && (
        <div className='toast-modal'>
          <p>Successfully added feedback!</p>
          <button onClick={() => {
            setShowToast(false)
            window.location.reload()
          }}>Close</button>
        </div>
      )}
    </div>
  );
}

export default App;

/*
This file demos how to use input fields and track their values without
useRef -- we can instead use useState and the onChange attribute of 
input elements.
*/
import './App.css';
import {Band} from './Band.js';
import {useState, useRef} from 'react';

function App() {
  const [bandNames, setBandNames] = useState(["The Wonder Years"]);
  const [inputText, setInputText] = useState("");

  function handleClick() {
    const val = inputRef.current.value;
    const newBandNames = [...bandNames, val];
    setBandNames(newBandNames);
    inputRef.current.value = "";
  }
  return (
    <div className="App">
      <h1>Bands I am seeing Friday</h1>
      <ul>
        {bandNames.map(bandName => <Band name={bandName}/>)}
      </ul>
      <input type="text" value={inputText} onChange={(e) => setInputText(e.target.value)}/>
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
}

export default App;

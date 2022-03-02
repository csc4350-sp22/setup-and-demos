import './App.css';
import {Band} from './Band.js';
import {useState, useRef} from 'react';

function App() {
  const [bandNames, setBandNames] = useState(["The Wonder Years"]);
  const inputRef = useRef(null);

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
      <input type="text" ref={inputRef} data-testid="input-field"/>
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
}

export default App;

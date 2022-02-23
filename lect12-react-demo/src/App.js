import './App.css';
import {Band} from './Band.js';

function App() {
  let bandName = "The Wonder Years";
  return (
    <div className="App">
      <h1>Bands I am seeing Friday</h1>
      <ul>
        <Band name={bandName}/>
        <Band name="Origami Angel"/>
        <Band name="Spanish Love Songs"/>
        <Band name="Save Face"/>
      </ul>
      // This line doesn't do anything yet! Why?
      <button onClick = {() => {bandName = "The Wonder Months"}}>Click me!</button>
    </div>
  );
}

export default App;

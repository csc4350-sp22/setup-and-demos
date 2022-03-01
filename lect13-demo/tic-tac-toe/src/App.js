import './App.css';
import {useState} from 'react';

function Square(props) {
  // condition ? (thing to do if true) : (thing to do if false)
  // Data down, action up
  return (
    <button className="square" onClick={props.onClickSquare}>
      {props.value}
    </button>
  );
}

function Board() {
  const [squares, setSquares] = useState(Array(9).fill(null));
  const [currPlayer, setCurrPlayer] = useState("X");
  const [winner, setWinner] = useState(null);

  function handleClick(i) {
    if (winner !== null || squares[i] !== null) {
      return;
    }
    const newSquares = squares.slice();
    newSquares[i] = newSquares[i] === null ? currPlayer : newSquares[i];
    const newWinner = computeWinner(newSquares);
    setWinner(newWinner);
    setSquares(newSquares);
    setCurrPlayer(currPlayer === "X" ? "O" : "X");
  }

  function computeWinner(squares) {
    const winningCombos = [
      [0,1,2],
      [3,4,5],
      [6,7,8],
      [0,3,6],
      [1,4,7],
      [2,5,8],
      [0,4,8],
      [2,4,6],
    ];
    for (const combo of winningCombos) {
      if (
        squares[combo[0]] !== null &&
        squares[combo[0]] === squares[combo[1]] &&
        squares[combo[1]] === squares[combo[2]]
      ) {
        return squares[combo[0]];
      }
    }
    return null;
  }

  function renderSquare(i) {
    return <Square value={squares[i]} onClickSquare={() => handleClick(i)}/>;
  }
  const status = winner === null ? `Next player: ${currPlayer}` : `Winner is ${winner}!`;

  return (
    <div>
      <div className="status">{status}</div>
      <div className="board-row">
        {renderSquare(0)}
        {renderSquare(1)}
        {renderSquare(2)}
      </div>
      <div className="board-row">
        {renderSquare(3)}
        {renderSquare(4)}
        {renderSquare(5)}
      </div>
      <div className="board-row">
        {renderSquare(6)}
        {renderSquare(7)}
        {renderSquare(8)}
      </div>
    </div>
  );
}

function Game() {
  return (
    <div className="game">
      <div className="game-board">
        <Board />
      </div>
      <div className="game-info">
        <div>{/* status */}</div>
        <ol>{/* TODO */}</ol>
      </div>
    </div>
  );
}


export default Game;
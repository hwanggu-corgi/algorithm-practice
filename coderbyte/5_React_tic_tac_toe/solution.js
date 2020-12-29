import React, { useState } from 'react';
import ReactDOM from 'react-dom';

const rowStyle = {
  display: 'flex'
}

const squareStyle = {
  'width':'60px',
  'height':'60px',
  'backgroundColor': '#ddd',
  'margin': '4px',
  'display': 'flex',
  'justifyContent': 'center',
  'alignItems': 'center',
  'fontSize': '20px',
  'color': 'white'
}

const boardStyle = {
  'backgroundColor': '#eee',
  'width': '208px',
  'alignItems': 'center',
  'justifyContent': 'center',
  'display': 'flex',
  'flexDirection': 'column',
  'border': '3px #eee solid'
}

const containerStyle = {
  'display': 'flex',
  'alignItems': 'center',
  'flexDirection': 'column'
}

const instructionsStyle = {
  'marginTop': '5px',
  'marginBottom': '5px',
  'fontWeight': 'bold',
  'fontSize': '16px',
}

const buttonStyle = {
  'marginTop': '15px',
  'marginBottom': '16px',
  'width': '80px',
  'height': '40px',
  'backgroundColor': '#8acaca',
  'color': 'white',
  'fontSize': '16px',
}

class Square extends React.Component {
  render() {
    return (
      <div
        className="square"
        style={squareStyle}>
      </div>
    );
  }
}

class Board extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      board: [['','',''],['','',''],['','','']],
      turn: 1,
      winner: -1
    }
  }

  updateBoard = (turn, coord) => {
    let i = coord[0];
    let j = coord[1];

    if (this.state.board[i][j] != '') {
      return;
    }

    this.setState((state, props) => {
      state.board[i][j] = turn == 1 ? 'X' : 'O';
      return state;
    });

    if (this.check(this.state.board)) {
      this.setState((state, props) => {
        state.winner = turn;
        return state;
      });
    }
  }

  render() {
    return (
      <div style={containerStyle} className="gameBoard">
        <div className="status" style={instructionsStyle}>Next player: {this.state.turn}</div>
        <div className="winner" style={instructionsStyle}>{this.state.winner > 0 ? `Winner: Player ${this.state.winner}` : `Winner: None`}</div>
        <button style={buttonStyle}>Reset</button>
        <div style={boardStyle}>
          <div className="board-row" style={rowStyle}>
            <Square onClick={e => this.updateBoard(this.state.turn, [0,0])}/>
            <Square onClick={e => this.updateBoard(this.state.turn, [0,1])}/>
            <Square onClick={e => this.updateBoard(this.state.turn, [0,2])}/>
          </div>
          <div className="board-row" style={rowStyle}>
            <Square onClick={e => this.updateBoard(this.state.turn, [1,0])}/>
            <Square onClick={e => this.updateBoard(this.state.turn, [1,1])}/>
            <Square onClick={e => this.updateBoard(this.state.turn, [1,2])}/>
          </div>
          <div className="board-row" style={rowStyle}>
            <Square onClick={e => this.updateBoard(this.state.turn, [2,0])}/>
            <Square onClick={e => this.updateBoard(this.state.turn, [2,1])}/>
            <Square onClick={e => this.updateBoard(this.state.turn, [2,2])}/>
          </div>
        </div>
      </div>
    );
  }
}

class Game extends React.Component {
  render() {
    return (
      <div className="game">
        <div className="game-board">
          <Board />
        </div>
      </div>
    );
  }
}

ReactDOM.render(
  <Game />,
  document.getElementById('root')
);
import React, { useState } from 'react';
import ReactDOM from 'react-dom';

class Counter extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        count: 0
    }
  }

  handleClick = () => {
    this.setState((state, props) => {
        return {
            count: state.count + 1
        }
    })
  }

  render() {
    return (
      <div id="mainArea">
        <p>button count: <span>{this.state.count}</span></p>
        <button onClick={this.handleClick} id="mainButton">Increase</button>
      </div>
    );
  }
}

ReactDOM.render(
  <Counter />,
  document.getElementById('root')
);
import React, { useState } from 'react';
import ReactDOM from 'react-dom';

class Counter extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div id="mainArea">
        <p>button count: <span>0</span></p>
        <button id="mainButton">Increase</button>
      </div>
    );
  }
}

ReactDOM.render(
  <Counter />,
  document.getElementById('root')
);
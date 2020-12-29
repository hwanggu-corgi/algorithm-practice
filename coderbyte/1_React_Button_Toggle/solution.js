import React, { useState } from 'react';
import ReactDOM from 'react-dom';

class Toggle extends React.Component {
  constructor(props) {
    super(props);
  }

  handleClick() {
    // todo
  }

  render() {
    return (
      <button>{this.state.buttonLabel}</button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
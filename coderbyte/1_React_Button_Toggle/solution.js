import React, { useState } from 'react';
import ReactDOM from 'react-dom';

class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        toggled: false
    }

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState( (state, props) => {
        return {
          toggled: !state.toggled
        }
    })
  }

  render() {
    return (
      <button onClick={this.handleClick}>{this.state.toggled ? "OFF" : "ON"}</button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
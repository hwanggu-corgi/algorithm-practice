import React, { useState } from 'react';
import ReactDOM from 'react-dom';

function DataList(props) {
  return (
    <h2>
      <ul>
        {props.data.map(item => (
          <li>
            <span>{item.name}</span>
            <span>{item.age}</span>
          </li>
        ))}
      </ul>
    </h2>
  );
}

const data = [
  { name: 'Daniel', age: 25 },
  { name: 'John', age: 24 },
  { name: 'Jen', age: 31 },
];

ReactDOM.render(
  <DataList data={ data } />,
  document.getElementById('root')
);
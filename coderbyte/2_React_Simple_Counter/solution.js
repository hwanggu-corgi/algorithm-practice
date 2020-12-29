import React, { useState } from 'react';
import ReactDOM from 'react-dom';

const style = {
  table: {
    borderCollapse: 'collapse'
  },
  tableCell: {
    border: '1px solid gray',
    margin: 0,
    padding: '5px 10px',
    width: 'max-content',
    minWidth: '150px'
  },
  form: {
    container: {
      padding: '20px',
      border: '1px solid #F0F8FF',
      borderRadius: '15px',
      width: 'max-content',
      marginBottom: '40px'
    },
    inputs: {
      marginBottom: '5px'
    },
    submitBtn: {
      marginTop: '10px',
      padding: '10px 15px',
      border:'none',
      backgroundColor: 'lightseagreen',
      fontSize: '14px',
      borderRadius: '5px'
    }
  }
}

function PhoneBookForm({ addEntryToPhoneBook }) {
  return (
    <form onSubmit={e => {e.preventDefault(); addEntryToPhoneBook(e)}} style={style.form.container}>
      <label>First name:</label>
      <br />
      <input
        style={style.form.inputs}
        className='userFirstname'
        name='userFirstname'
        type='text'
      />
      <br/>
      <label>Last name:</label>
      <br />
      <input
        style={style.form.inputs}
        className='userLastname'
        name='userLastname'
        type='text'
      />
      <br />
      <label>Phone:</label>
      <br />
      <input
        style={style.form.inputs}
        className='userPhone'
        name='userPhone'
        type='text'
      />
      <br/>
      <input
        style={style.form.submitBtn}
        className='submitButton'
        type='submit'
        value='Add User'
      />
    </form>
  )
}

function InformationTable(props) {
  return (
    <table style={style.table} className='informationTable'>
      <thead>
        {
            props.data.map(item => (
                <tr>
                    <th style={style.tableCell}>{item.userFirstname}</th>
                    <th style={style.tableCell}>{item.userLastname}</th>
                    <th style={style.tableCell}>{item.userPhone}</th>
                </tr>
            ))
        }
      </thead>
    </table>
  );
}

class Application extends React.Component {
  constructor() {
    this.state = {
      phoneList: []
    }
  }

  addEntryToPhoneBook = (e) => {
    const data = new FormData(e.target);
    const item = {
        userFirstname: data.get("userFirstname"),
        userLastname: data.get("userLastname"),
        userPhone: data.get("userPhone")
    };

    this.setState((state, props) => {
        return {
            phoneList: state.phoneList.push(entry)
        }
    })
  }

  render() {
    return (
      <section>
        <PhoneBookForm addEntryToPhoneBook={this.addEntryToPhoneBook} />
        <InformationTable data={this.state.phoneList} />
      </section>
    );
  }
}

ReactDOM.render(
  <Application />,
  document.getElementById('root')
);
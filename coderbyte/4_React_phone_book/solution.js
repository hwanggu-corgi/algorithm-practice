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
        value='Coder'
        name='userFirstname'
        type='text'
      />
      <br/>
      <label>Last name:</label>
      <br />
      <input
        style={style.form.inputs}
        className='userLastname'
        value='Byte'
        name='userLastname'
        type='text'
      />
      <br />
      <label>Phone:</label>
      <br />
      <input
        style={style.form.inputs}
        className='userPhone'
        value='8885559999'
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
  let data = props.data.sort((a,b) => {
    if (a.userLastname.toUpperCase() < b.userLastname.toUpperCase()) {
        return -1;
    }

    if (a.userLastname.toUpperCase() > b.userLastname.toUpperCase()) {
        return 1;
    }

    return 0
  });

  return (
    <table style={style.table} className='informationTable'>
        <thead>
        <tr>
          <th style={style.tableCell}>First name</th>
          <th style={style.tableCell}>Last name</th>
          <th style={style.tableCell}>Phone</th>
        </tr>
      </thead>
      <tbody>
        {
            data.map((item,index) => (
                <tr key={index}>
                    <th style={style.tableCell}>{item.userFirstname}</th>
                    <th style={style.tableCell}>{item.userLastname}</th>
                    <th style={style.tableCell}>{item.userPhone}</th>
                </tr>
            ))
        }
      </tbody>
    </table>
  );
}

class Application extends React.Component {
  constructor(props) {
    super(props);
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
        state.phoneList.push(item);
        return state;
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
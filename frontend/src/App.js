import {useEffect, useState} from 'react';
import axios from 'axios';
//import {format} from "date-fns"

import './App.css';

const baseurl = "http://localhost:5000";

function App() {

  const [price, setPrice] = useState("");
  const [eventsList, setEventsList] = useState([]);

  const fetchEvents = async () => {
    const data = await axios.get(`${baseurl}/events`)
    const {events} = data.data
    setEventsList(events);
    console.log("data: ", data)
  }

  const handleChange = e => {
    setPrice(e.target.value);
  }

  const handleSubmit = e => {
    e.preventDefault();
    console.log(price);
  }

  useEffect(() => {
    fetchEvents();
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <form onSubmit={handleSubmit}>
          <label htmlFor='price'>Price</label>
          <input onChange={handleChange} type="text" name="price" id="price" value={price} />
          <button type='submit'>Submit</button>
        </form>

      </header>
    </div>
  );
}

export default App;

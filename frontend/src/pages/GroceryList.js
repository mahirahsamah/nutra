import React, { useState, useEffect } from "react";
import axios from 'axios';
import './Recipes.css';
import { Header } from './../components/'
import './Style.css';
import './../components/Modal/Modal.css'

function ButtonList(props) {
  const buttonData = props.buttonData;

  return (
    <div>
      {buttonData.map((item, index) => (
        <button key={index} onClick={() => console.log(item)}>
          {item}
        </button>
      ))}
    </div>
  );
}

function GroceriesPage() {

    const [grocery_lists, set_grocery_lists] = useState([]);
    const [num_weeks, set_num_weeks] = useState([]);

    const [modal, setModal] = useState(false);

    const toggleModal=()=>{
      setModal(!modal)
      console.log(modal);
    }

    const [selectedIndex, setSelectedIndex] = useState(null);
    const handleClick = index => {
      setSelectedIndex(index);
    };
  
    useEffect(() => {
      const curruserID = localStorage.getItem("curruserID");

      const get_num_weeks  = async () => {
        axios.get(`http://127.0.0.1:5000/get_num_weeks/${curruserID}`)
        .then(response => {
          set_num_weeks(response.data);
          get_grocery_list(response.data);
        })
        .catch(error => {
            console.error(error);
        });
      };

    
      const get_grocery_list = async (num_weeks) => {
        const groceryArray = [];
        const n_int = parseInt(num_weeks, 10);
  
        for (let i = 1; i < n_int+1; i++) {
          const response = await fetch(`http://127.0.0.1:5000/get_grocery_list/${curruserID}/${i}`);
          const data = await response.json();

          groceryArray.push(data);
          //groceryArray.push({ ...data[i], id: i});
        }
  
        set_grocery_lists(groceryArray);
        console.log(groceryArray);
        
      };
      
      get_grocery_list();
      get_num_weeks();

    }, []);

    const n = num_weeks;
    const n_int = parseInt(n, 10);

    const buttonNums = Array.from({ length: n_int }, (_, index) => index + 1);
    const buttonArray = buttonNums.map(item => 'Week ' + item);
    const buttonContent = grocery_lists;

  return (
    <div>
      <div style={{paddingBottom:"10vh"}} className="App" ><Header /></div>   




      <div>
        {buttonArray.map((name, index) => (
          <button onClick={() => {
            toggleModal();
            handleClick(index);
          }} className="btn-modal" key={index} >
            {name}
          </button>
        ))}
      </div>

      {modal && (
        <div className="modal">
          <div onClick={toggleModal} className="overlay">
            <div className="modal-content">
              <h2>grocery list</h2>
              {selectedIndex !== null && (
                <div>
                  <p>{grocery_lists[selectedIndex].ginger}</p>
                </div>
              )}
              <button className="close-modal" onClick={toggleModal}> close </button>
            </div>
          </div>
        </div>
      )}

    </div>  
  );
}

export default GroceriesPage;
import React, { useState, useEffect } from "react";
import axios from 'axios';
import './Recipes.css';
import { Header } from './../components/'
import './Style.css';
import './../components/Modal/Modal.css'

function MyComponent({ myData, id }) {
  //const backend = "http://localhost:3000/ingredient/";
  const myObject = myData[id];

  if (!myObject) {
    return <div>Object with id {id} not found</div>;
  }

  const objectElements = Object.entries(myObject).map(([key, value]) => {
    const backend = "http://localhost:3000/ingredient/" + key;
    return <div key={key}><a href={backend}>{key}</a>: {value}</div>;
  });

  return <div>{objectElements}</div>;
}

function GroceriesPage() {
    const backend = "http://localhost:5000";

    const [grocery_lists, set_grocery_lists] = useState([]);
    const [num_weeks, set_num_weeks] = useState([]);
    const [weeks_list, set_weeks_list] = useState([]);
    const [gls_list, set_gls_list] = useState([]);

    const [modal, setModal] = useState(false);

    const toggleModal=()=>{
      setModal(!modal)
      console.log(modal);
    }

    const [selectedIndex, setSelectedIndex] = useState(null);
    const handleClick = index => {
      setSelectedIndex(index);
    };

    useEffect(()=>{
      const curruserID = localStorage.getItem("curruserID");
      
    })
  
    useEffect(() => {
      const curruserID = localStorage.getItem("curruserID");

      const get_num_weeks  = async () => {
        axios.get(`${backend}/get_num_weeks/${curruserID}`) //${backend}/getuserinfo?user=${currentUser}
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
          const response = await fetch(`${backend}/get_grocery_list/${curruserID}/${i}`);
          const data = await response.json();

          groceryArray.push(data);
          //groceryArray.push({ ...data[i], id: i});
        }
  
        set_grocery_lists(groceryArray);
        //console.log(groceryArray);
        
      };

      const get_weeks_list  = async () => {
        axios.get(`${backend}/get_user_grocery_lists/${curruserID}`) //${backend}/getuserinfo?user=${currentUser
        .then(response => {
          
          const wks_keys = Object.keys(response.data);
          const gl_values = Object.values(response.data);

          console.log(gl_values);
          
          set_weeks_list(wks_keys);
          set_gls_list(gl_values);
        })
        .catch(error => {
            console.error(error);
        });
      };
      
      get_grocery_list();
      get_num_weeks();
      get_weeks_list();

    }, []);

    const n = num_weeks;
    const n_int = parseInt(n, 10);

    const buttonNums = Array.from({ length: n_int }, (_, index) => index + 1);
    const buttonArray = weeks_list.map(item => 'Week ' + item);

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
              {selectedIndex !== null && (
                <div key={selectedIndex}>
                  
                  <h2>Grocery List for Week {selectedIndex}</h2>
                  
                  <MyComponent myData={gls_list} id={selectedIndex} />

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
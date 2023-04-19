import styled from 'styled-components';
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import './Recipes.css';
import { Header } from './../components/'
import './Style.css';


function GroceriesPage() {
  const [grocery_list, set_grocery_list] = useState(null);
  const [num_weeks, set_num_weeks] = useState(null);
  
  const curruserID = localStorage.getItem("curruserID");
    useEffect(() => {
      const get_grocery_list  = async () => {
        axios.get(`http://127.0.0.1:5000/get_grocery_list/${curruserID}/2`)
        .then(response => {
          set_grocery_list(response.data);
        })
        .catch(error => {
            console.error(error);
        });
      };

      const get_num_weeks  = async () => {
        axios.get(`http://127.0.0.1:5000/get_num_weeks/${curruserID}`)
        .then(response => {
          set_num_weeks(response.data);
        })
        .catch(error => {
            console.error(error);
        });
      };

      get_grocery_list();
      get_num_weeks();

  }, []);

  return (
    <div>
    <div style={{paddingBottom:"10vh"}} className="App" ><Header /></div>
      <h1>Dictionary Data:</h1>
      <p>{num_weeks}</p>
      
      <ul>
        {Object.keys(grocery_list).map((key) => (
          <li key={key}>
            {key}: {grocery_list[key]}
          </li>
        ))}
      </ul>

    </div>  
  );
}

export default GroceriesPage;
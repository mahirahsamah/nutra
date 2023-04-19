import styled from 'styled-components';
import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import './Recipes.css';
import { Header } from './../components/'
import './Style.css';


const Container = styled.div`
  background-color: #f0f0f0;
  padding: 20px;
`;

const Title = styled.h1`
  font-size: 32px;
  color: #333;
`;

const Paragraph = styled.p`
  font-size: 18px;
  line-height: 1.5;
`;

function GroceriesPage() {
  const [data, setData] = useState([]);
  
  const curruserID = localStorage.getItem("curruserID");
  useEffect(() => {
      axios.get(`http://127.0.0.1:5000/get_grocery_list/${curruserID}/1`)
      .then(response => {
          setData(response.data);
      })
      .catch(error => {
          console.error(error);
      });
  }, []);

  return (
    <div>
    <div style={{paddingBottom:"10vh"}} className="App" ><Header /></div>
      <h1>Dictionary Data:</h1>
      <ul>
        {Object.keys(data).map((key) => (
          <li key={key}>
            {key}: {data[key]}
          </li>
        ))}
      </ul>
    </div>  
  );
}

export default GroceriesPage;
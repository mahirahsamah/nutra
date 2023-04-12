import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';
import { Header } from './../components/'
import land1 from "../images/land.jpg";
import land2 from "../images/land2.jpg";
import './Style.css';
function Ingredient() {

     return (
          <div style={{paddingBottom:"10vh"}} className="App" >
               <Header />
          </div>
          //<div> Hello { localStorage.getItem('curruser') }!! </div>
     );

}

export default Ingredient;
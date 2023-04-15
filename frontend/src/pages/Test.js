import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';
import { Header } from './../components/'
import land1 from "../images/land.jpg";
import land2 from "../images/land2.jpg";
import { Link } from 'react-router-dom';
import './Style.css';

function Test() {
    

    const [passed, updateSearch] = useState();

    
 

    return (
        <div style={{paddingBottom:"10vh"}} className="App" >
            <Header />
            <input type="text" onChange = {(e)=>{updateSearch(e.target.value);}}></input>
            <Link to={"/ingredient/" + passed}>
                Search API
            </Link>
        </div>
        //<div> Hello { localStorage.getItem('curruser') }!! </div>
    );

}

export default Test;
import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';
import { Header } from './../components/'
import land1 from "../images/land.jpg";
import land2 from "../images/land2.jpg";
import './Style.css';

function Ingredient() {
    

    const [search,updateSearch] = useState();
    const [results, setResults] = useState([]);

    const apiCall =() =>{
        // set up the request parameters
        const params = {
            api_key: "95EADE36B4524431B70F2249197BBA99",
            search_term: search,
            category_id: "5xt1a",
            type: "search"
        }
        // make the http GET request to RedCircle API
        axios.get('https://api.redcircleapi.com/request', { params })
        .then(response => {
            // print the JSON response from RedCircle API
            console.log(JSON.stringify(response.data, 0, 2));
            setResults(response.data.search_results);
        }).catch(error => {
        // catch and print the error
        console.log(error);
        })
    }
 

    return (
        <div style={{paddingBottom:"10vh"}} className="App" >
            <Header />
            <input type="text" onChange = {(e)=>{updateSearch(e.target.value);}}></input>
            <button onClick={()=>apiCall()}>Search</button>
            {results.map((val)=> (
                <div style={{display:"flex", width:"40vw", margin:"10vh", backgroundColor:"rgb(225, 247, 217)"}}> 
                    <label>{val.product.title}</label>
                    <img style={{height:"70%", width:"70%"}} src = {val.product.main_image}></img>
                    <label>Price: ${val.offers.primary.price}</label>
                    <button>Select</button>
                </div>
                
            ))}
        </div>
        //<div> Hello { localStorage.getItem('curruser') }!! </div>
    );

}

export default Ingredient;
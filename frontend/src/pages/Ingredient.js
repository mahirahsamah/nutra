import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';
import { Header } from './../components/'
import land1 from "../images/land.jpg";
import land2 from "../images/land2.jpg";
import { Link } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import { useEffect } from "react";
import { useParams } from "react-router-dom";

import './Ingredient.css';

function Ingredient() {
    const backend = "http://localhost:5000"

    const [search,updateSearch] = useState();
    const [results, setResults] = useState([]);
    // const location = useLocation();
    const {term} = useParams();
    // const searchButton = document.getElementById('searchButton')
    const navigate = useNavigate();
    // updateSearch("Search Term");

    useEffect(() => {

        if(term != undefined){
            updateSearch(term)
            console.log("Search Value: "+ search);
            

            // set up the request parameters
            const params = {
                api_key: "95EADE36B4524431B70F2249197BBA99",
                search_term: term,
                category_id: "5xt1a",
                type: "search"
            }

            console.log("Params: "+ params.search_term)
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
    
        // console.log("Term Value: "+ term);
        // console.log("Search Value: " + search)
      });


    const apiCall =() =>{
        console.log(search)
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

    const updateLink =() =>{
        axios.put(`${backend}/updatelink`)
        navigate('/groceries-page');
    }
 

    return (
        <div style={{paddingBottom:"10vh", textAlign:"center"}} className="App" >
            <Header />
            <input type="text" class="input_field" placeholder={search}  onChange = {(e)=>{updateSearch(e.target.value);}}></input>
            <button className="searchButton" id="searchButton" onClick={()=>apiCall()}>Search</button>
            <main>
            <section class="cards" style={{paddingTop:"10vh", textAlign:"center"}}>
            {results.map((val)=> (
                // <div style={{display:"flex", width:"40vw", margin:"10vh", backgroundColor:"rgb(225, 247, 217)"}}> 
                //     <label>{val.product.title}</label>
                //     <img style={{height:"70%", width:"70%"}} src = {val.product.main_image}></img>
                //     <label>Price: ${val.offers.primary.price}</label>
                //     <button>Select</button>
                // </div>
                
                    <div class="card" style={{textAlign:"center"}} onClick={updateLink}>
                        <div class="card__image-container">
                            <img
                            src={val.product.main_image}
                            />
                        </div>
                        <div class="card__content">
                            <p class="card__title text--medium">
                                {val.product.title}
                            </p>
                            <div class="card__info">
                            <p class="text--medium">Rating: {val.product.rating} ({val.product.ratings_total})</p>
                            <p class="card__price text--medium">${val.offers.primary.price}</p>
                            </div>
                        </div>
                    </div>
            ))}
            </section>
            </main>
        </div>
        //<div> Hello { localStorage.getItem('curruser') }!! </div>
    );

}

export default Ingredient;
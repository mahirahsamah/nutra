import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';
import { Header } from './../components/'
import land1 from "../images/land.jpg";
import land2 from "../images/land2.jpg";
import foods from "../images/foods.png";
import './Style.css';
function LandingPage() {
     
     // renderName = () => {
     //      return localStorage.getItem('nameone');
     //      // innerHtml 
     // };
     //Hello { localStorage.getItem('curruser') }!!

     return (
          <div style={{paddingBottom:"10vh"}} className={classes.App} >
               <Header />
               
               <div  className={classes.imgs} style={{display:"flex", margin:"3vw"}}>
                    <div>
                         <img style={{height:"100%", width: "100%"}} src={foods}></img>
                    </div>
                   
               </div>

               <div style = {{display:"flex"}}>
                    <div className={classes.intro}>
                         <h1 className={classes.introh1} >Welcome to Nutra!</h1>
                         <p style={{ width: '500px' }}>Nutra is designed to provide you with a personalized meal plan that fits your weekly nutritional needs, helping you to achieve your health goals in an easy and enjoyable way.</p>

                         <p className={classes.introp2}>Here, you can browse a wide variety of recipes and select the ones that meet your dietary requirements, preferences, and goals.</p>
                         <p className={classes.introp3}>Nutra generates a grocery list based on the ingredients needed for each recipe.</p>
                         <p className={classes.introp4}>Nutra is perfect for anyone trying to live a healthier life!</p>
                    </div>
               </div>
          </div>
          //<div> Hello { localStorage.getItem('curruser') }!! </div>
     );

}

export default LandingPage;
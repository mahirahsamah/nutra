import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Landing.module.css';
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
                         <img style={{height:"100%", width: "100%"}} src={land1}></img>
                    </div>
                    <div>
                         <img style={{height:"100%", width: "100%"}} src={land2}></img>
                    </div>
               </div>
               <h1 className={classes.introh1} >Welcome to Nutra!</h1><br></br><br></br>
               <div className={classes.intro} >
                    
                    Nutra is designed to provide you with a personalized meal plan that fits your weekly nutritional needs, helping you to achieve your health goals in an easy and enjoyable way.

                    Here, you can browse a wide variety of recipes and select the ones that meet your dietary requirements, preferences, and goals.
                    Nutra generates a grocery list based on the ingredients needed for each recipe.
                    Nutra is perfect for anyone trying to live a healthier life!
                    
               </div>
               <br></br><br></br><br></br><br></br>
               <div style = {{display:"flex"}}>
                    <div className="blurb">
                         "Nutra is a great recipe app that I use frequently. I appreciate the app's user-friendly interface, which makes it easy to search for recipes and save them for later. The app has a vast database of recipes, so there's always something new to try."
                    </div>
                    <div className="blurb"> 
                         "Nutra is an excellent recipe app that offers thousands of recipes for every type of cuisine. The app's interface is straightforward to use and has a great visual appeal. Each recipe comes with a video tutorial, which makes it easier to understand the cooking process. One thing I love about Nutra is that you can customize recipes according to the number of servings required."
                    </div>
                    <div className="blurb">
                         "Nutra is a recipe app that I've been using for years. The app is fantastic for finding recipes based on your dietary restrictions and preferences. Nutra has a feature that suggests recipes based on your past search history, making it easier to find something you'll like"
                    </div>
               </div>
               
               {/* <div  className={classes.imgs} style={{display:"flex", margin:"3vw"}}>
                    <div>
                         <img style={{height:"100%", width: "100%"}} src={foods}></img>
                    </div>
                   
               </div>

               
               <div className={classes.intro}>
                    <div>
                         <h1 className={classes.introh1} >Welcome to Nutra!</h1>
                         <p>Nutra is designed to provide you with a personalized meal plan that fits your weekly nutritional needs, helping you to achieve your health goals in an easy and enjoyable way.

                         Here, you can browse a wide variety of recipes and select the ones that meet your dietary requirements, preferences, and goals.
                         Nutra generates a grocery list based on the ingredients needed for each recipe.
                         Nutra is perfect for anyone trying to live a healthier life!</p>
                    </div>
               </div>
   */}
          </div>
          //<div> Hello { localStorage.getItem('curruser') }!! </div>
     );

}

export default LandingPage;
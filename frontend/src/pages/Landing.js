import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';

function LandingPage() {
     
     // renderName = () => {
     //      return localStorage.getItem('nameone');
     //      // innerHtml 
     // };

     return (
          <div> Hello { localStorage.getItem('curruser') }!! </div>
     );

}

export default LandingPage;
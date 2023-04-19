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
  return (
    
    <div style={{paddingBottom:"10vh"}} className="App" >
               <Header />

          </div>
  );
}

export default GroceriesPage;
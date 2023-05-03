import React from 'react';

import './navbar.css'

function Navbar () {

  return (
    <section className="navbar">
      <a href="/home" className="navbar-item">Home</a>
      <a href="/recipes-page" className="navbar-item">Recipes</a>
      <a href="/groceries-page" className="navbar-item">Grocery Lists</a>
      <a href="/ingredient" className="navbar-item">Ingredients</a>
      <a href="/profile" className="navbar-item">Profile</a>
      <a href="/" className="navbar-item">Logout</a>
  </section>
  )

}

export default Navbar;
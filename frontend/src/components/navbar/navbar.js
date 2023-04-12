import React from 'react';

import './navbar.css'

function Navbar () {

  return (
    <section className="navbar">
      <a href="/home" className="navbar-item">Home</a>
      <a href="/home" className="navbar-item">Recipe</a>
      <a href="/home" className="navbar-item">Grocery List</a>
      <a href="/home" className="navbar-item">Ingredients</a>
      <a href="/profile" className="navbar-item">Profile</a>
      <a href="/" className="navbar-item">Logout</a>
  </section>
  )

}

export default Navbar;
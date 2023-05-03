import React from 'react';
import { Navbar } from '../../components' ;

import './header.css';

function Header () {

  return (
    <section className="header">
      <section className="header-bottom">
        <section className="header-bottom__email">
          nutra@gmail.com
        </section>
      </section>
      
      <section className="header-top">
        
        <section className="header-top__logo">
          <a href="/landing-page" className="header-logo">NUTRA</a>
        </section>
        <section className="header-top__navbar">
          <section className="header-top__navigation">
            <Navbar />
          </section>
          <hr className="header-top__seperator" />
        </section>
      </section>
      
    </section>
  )
}

export default Header;
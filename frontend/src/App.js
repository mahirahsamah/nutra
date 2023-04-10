import { Route, Routes } from 'react-router-dom';


import LoginPage from './pages/Login';
import SignupPage from './pages/Signup';
import LandingPage from './pages/Landing';

function App() {
  return (

    <Routes>
      <Route path='/' element = {<LoginPage/>} />
      <Route path='/signup-page' element = {<SignupPage/>} />
      <Route path='/landing-page' element = {<LandingPage/>} />
    </Routes>


    // <div className="App">
    //   <section>
    //     <form onSubmit={handleSubmit}>
    //       <label htmlFor='price'>Price</label>
    //       <input onChange={handleChange} type="text" name="price" id="price" value={price} />
    //       <button type='submit'>Submit</button>
    //     </form>
    //   </section>
    //   <section>
    //     <ul>
    //       {eventsList.map(event  => {
    //         return (
    //           <li key={event.itemID}>{event.price}</li>
    //         )
    //       })}
    //     </ul>
    //   </section>
    // </div>

  );
}

export default App;

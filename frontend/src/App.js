import { Route, Routes } from 'react-router-dom';


import LoginPage from './pages/Login';
import SignupPage from './pages/Signup';
import Home from './pages/Landing';
import Profile from './pages/Profile';
import Ingredients from './pages/Ingredient';
import RecipesPage from './pages/Recipes';

function App() {
  return (

    <Routes>
      <Route path='/' element = {<LoginPage/>} />
      <Route path='/signup' element = {<SignupPage/>} />
      <Route path='/home' element = {<Home/>} />
      <Route path='/profile' element = {<Profile/>} />
      <Route path='/recipes-page' element = {<RecipesPage/>} />
      <Route path ='/ingredient' element = {<Ingredients/>}/>
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

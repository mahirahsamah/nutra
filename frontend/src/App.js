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

  );
}

export default App;

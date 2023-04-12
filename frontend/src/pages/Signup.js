
import React, { useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';


const SignupPage = () => {
     const backend = "http://localhost:5000"
     const [email, setEmail] = useState("");
     const [username, setUsername] = useState("");
     const [password, setPassword] = useState("");
     const navigate = useNavigate();

     const handleMakeAccount = async () => {
          const data = await axios.post(`${backend}/createuser?user=${username}&pass=${password}&email=${email}`)
          console.log(username.length)

          if(email.length === 0 || username.length === 0 || password.length === 0){
               alert("Missing field");
          }
          else if(data.data.user.length === 0){
               localStorage.setItem("curruser", username);
               navigate("/landing-page");
          } else {
               alert("Username already exist");
          }  
     };

     const goToLogin = () => {
          navigate("/");

     };

     return (
          <div className={classes.contained}>
               <div className={classes.login_box}>
                    <h1>Signup</h1>
                    <form>
                         <ul>
                              <li>
                                   <input
                                        type="text"
                                        placeholder="Email"
                                        className={classes.input_field}
                                        value={email}
                                        onChange={(e) => setEmail(e.target.value)}
                                   />
                              </li>
                              <li>
                                   <input
                                        type="text"
                                        placeholder="Username"
                                        className={classes.input_field}
                                        value={username}
                                        onChange={(e) => setUsername(e.target.value)}
                                   />
                              </li>

                              <li>
                                   <input
                                        type="password"
                                        placeholder="Password"
                                        className={classes.input_field}
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                   />
                              </li>
                              <li>
                                   <button type="button" className={classes.submit_button} onClick={handleMakeAccount}>
                                        Signup
                                   </button>
                              </li>
                              <li>
                                   <button type="button" className={classes.go_signup_button} onClick={goToLogin}>
                                        Have an account? Login now!
                                   </button>

                              </li>
                         </ul>
                    </form>
               </div>
          </div>
     );
};

export default SignupPage;

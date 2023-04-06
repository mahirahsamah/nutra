
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';


const LoginPage = () => {
     const [username, setUsername] = useState("");
     const [password, setPassword] = useState("");
     const navigate = useNavigate();

     const handleLogin = () => {

          if (username === "user" && password === "password") {
               navigate("/landing-page");
          } else {
               // Show error message if login fails
               alert("Invalid username or password.");
          }
     };

     const goToSignup = () => {
          navigate("/signup-page");

     };

     return (
          <div className={classes.contained}>
               <div className={classes.login_box}>
                    <h1>Login</h1>
                    {/* <form> */}
                         <ul>
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
                                   <button type="button" className={classes.submit_button} onClick={handleLogin}>
                                        Login
                                   </button>
                              </li>
                              <li>
                                   <button type="button" className={classes.go_signup_button} onClick={goToSignup}>
                                        Don't have an account? Make one now!
                                   </button>

                              </li>
                         </ul>
                    {/* </form> */}
               </div>
          </div>
     );
};

export default LoginPage;


import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';


const SignupPage = () => {
     const [username, setUsername] = useState("");
     const [password, setPassword] = useState("");
     const navigate = useNavigate();

     const handleMakeAccount = () => {

          alert("Save signup info");

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
                                        placeholder="Name"
                                        className={classes.input_field}
                                        value={username}
                                        onChange={(e) => setUsername(e.target.value)}
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

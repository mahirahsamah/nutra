import React, { useEffect, useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';


const LoginPage = () => {
     const backend = "http://localhost:5000"
     const [username, setUsername] = useState("");
     const [password, setPassword] = useState("");
     const [currWeek, setCurrWeek] = useState("");
     const [userCreatedDate, setUserCreatedDate]= useState("");

     const navigate = useNavigate();

     const uID = localStorage.getItem("curruserID");
     const date = axios.get(`${backend}/get_created_date/${uID}`)
     const dateString = '2022-01-01';
     //const created_date = '';

     useEffect(() => {
          const uID = localStorage.getItem("curruserID");
          const fetchData = async () => {
            const response = await axios.get(`${backend}/get_created_date/${uID}`);
            const userCreatedDate = response.data;
            setUserCreatedDate(userCreatedDate);
            //console.log(userCreatedDate)

            const userCreationDate = new Date(userCreatedDate); // replace with the actual date from your database
          const currentDate = new Date();
          const diffInMs = currentDate - userCreationDate;
          const wk = Math.floor(diffInMs / (7 * 24 * 60 * 60 * 1000));
          setCurrWeek(wk);
          };
          
          fetchData();
     }, []);

     localStorage.setItem("currWeek", currWeek);

     const handleLogin = async () => {
          const data = await axios.get(`${backend}/checklogin?user=${username}&pass=${password}`)
          
          //const date = axios.get(`${backend}/get_created_date/${curruserID}`)

          if(data.data.user.length === 0){
               alert("No matching username and password combo.");
          } else {
               localStorage.setItem("curruser", username);
               localStorage.setItem("curruserID", data.data.user[0].userID);

               navigate("/home");
          }

          

     };

     const goToSignup = () => {
          navigate("/signup");

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


import React, { useEffect,useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Login.module.css';


const SignupPage = () => {
     const backend = "http://localhost:5000"
     const [email, setEmail] = useState("");
     const [username, setUsername] = useState("");
     const [password, setPassword] = useState("");
     const [currWeek, setCurrWeek] = useState("");
     const [userCreatedDate, setUserCreatedDate]= useState("");
     const navigate = useNavigate();

     useEffect(() => {
          const uID = localStorage.getItem("curruserID");
          const fetchData = async () => {
            const response = await axios.get(`${backend}/get_created_date/${uID}`);
            const userCreatedDate = response.data;
            setUserCreatedDate(userCreatedDate);
            
            //console.log(userCreatedDate);

            const userCreationDate = new Date(userCreatedDate); // replace with the actual date from your database
          const currentDate = new Date();
          const diffInMs = currentDate - userCreationDate;
          const wk = Math.floor(diffInMs / (7 * 24 * 60 * 60 * 1000));
          setCurrWeek(wk);
          //console.log(wk);
          };
          
          fetchData();
     }, []);

     localStorage.setItem("currWeek", currWeek);

     const handleMakeAccount = async () => {
          const data = await axios.post(`${backend}/createuser?user=${username}&pass=${password}&email=${email}`)
          //console.log(data)

          if(email.length === 0 || username.length === 0 || password.length === 0){
               alert("Missing field");
          }
          else if(data.data.user.length === 0){
               localStorage.setItem("curruser", username);
               navigate("/profile");
          } else {
               alert("Username already exist");
          }  
     };



     const goToLogin = () => {
          navigate("/");

     };

     return (
          <div>
          <h1 className={classes.welcome}>Welcome to Nutra!</h1>
          <h2 className={classes.plslogin}>Please sign up:</h2>
          
          <div className={classes.contained}>
               <div className={classes.login_box}>
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
                                   <button type="button" className={classes.submit_button} onClick={goToLogin}>
                                        Have an account? Login now!
                                   </button>

                              </li>
                         </ul>
                    </form>
               </div>
               </div>
          </div>
     );
};

export default SignupPage;

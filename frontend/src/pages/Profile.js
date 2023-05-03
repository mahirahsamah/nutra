import React, { useEffect, useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Profile.module.css';
import { Header } from './../components/'



const ProfilePage = () => {

  const [data, setData] = useState('');
  const navigate = useNavigate();

  const currentUser = localStorage.getItem('curruser')
  const currentUserID = localStorage.getItem('curruserID')
  const backend = "http://localhost:5000"
  const [gender, setGender] = useState("");
  const [weight_lbs, setWeight_lbs] = useState("");
  const [age, setAge] = useState("");
  const [height_feet, setHeight_feet] = useState("");
  const [height_inches, setHeight_inches] = useState("");
  const [activity_level, setActivity_level] = useState("");
  const [vegetarian, setVegetarian] = useState("");
  const [vegan, setVegan] = useState("");
  const [gluten_free, setGluten_free] = useState("");
  const [keto, setKeto] = useState("");
  const [paleo, setPaleo] = useState("");
  const [pescetarian, setPescetarian] = useState("")
  const [preferences, setPreferences] = useState("");
  const [restrictions, setRestrictions] = useState("");
  const [userData, setUserData] = useState("");

  // useEffect(() => {
  //   async function fetchData(){
  //     const result = await axios.get(`${backend}/getuserinfo?user=${currentUser}`)
  //     setUserData(result.data.user[0])
  //     console.log(userData.gender)
  //   }
  //   fetchData()
  // })

  /*useEffect(async () => {
    const result = await axios.get(`${backend}/getuserinfo?user=${currentUser}`);
    setUserData(result.data.user[0]);
    setGender(result.data.user[0].gender);
    setWeight_lbs(result.data.user[0].weight_lbs);
    setAge(result.data.user[0].age);
    setHeight_feet(result.data.user[0].height_feet);
    setHeight_inches(result.data.user[0].height_inches);
    setActivity_level(result.data.user[0].activity_level);
    setVegetarian(result.data.user[0].vegetarian);
    setVegan(result.data.user[0].vegan);
    setGluten_free(result.data.user[0].gluten_free);
    setKeto(result.data.user[0].keto);
    setPaleo(result.data.user[0].paleo);
    setPescetarian(result.data.user[0].pescetarian);
    setPreferences(result.data.user[0].preferences);
    setRestrictions(result.data.user[0].restrictions);

    // console.log("test"+ gender);
  }, []);*/


  useEffect(async () => {
    const result = await axios.get(`${backend}/getuserinfo?user=${currentUser}`);
    setUserData(result.data.user[0]);
    setGender(result.data.user[0].gender);
    setWeight_lbs(result.data.user[0].weight_lbs);
    setAge(result.data.user[0].age);
    setHeight_feet(result.data.user[0].height_feet);
    setHeight_inches(result.data.user[0].height_inches);
    setActivity_level(result.data.user[0].activity_level);
    setVegetarian(result.data.user[0].vegetarian);
    setVegan(result.data.user[0].vegan);
    setGluten_free(result.data.user[0].gluten_free);
    setKeto(result.data.user[0].keto);
    setPaleo(result.data.user[0].paleo);
    setPescetarian(result.data.user[0].pescetarian);
    setPreferences(result.data.user[0].preferences);
    setRestrictions(result.data.user[0].restrictions);
  }, []);

  const update = async () => {
    
    const updateData = await axios.put(`${backend}/updateuser?user=${currentUser}&gender=${gender}&weight_lbs=${weight_lbs}&age=${age}&height_feet=${height_feet}&height_inches=${height_inches}&activity_level=${activity_level}&vegetarian=${vegetarian}&vegan=${vegan}&gluten_free=${gluten_free}&keto=${keto}&paleo=${paleo}&pescetarian=${pescetarian}&preferences=${preferences}&restrictions=${restrictions}`)

    const response = await axios.get(`${backend}/get_user_id/${currentUser}`);
    setData(response.data);
    //console.log(response.data);
    localStorage.setItem("curruserID", response.data);


    const post_nutrition = await axios.post(`${backend}/post_nutrition/${response.data}`);
    window.alert("Your profile was updated!");
  
};


useEffect(() => {
  update();

}, []);



  return (
    <div className="bg">
      <Header />
      <h1 className={classes.welcome}>Please fill out your information</h1>
    <div className={classes.contained}>
      <div className={classes.form}>
      
            <ul>
              <li key={userData.gender}>
                Gender:
                <input
                type="text"
                placeholder="gender"
                className={classes.input_field}
                value={gender}
                onChange={(e) => setGender(e.target.value)}
                />
              </li>

              <li key={userData.weight_lbs}>
                Weight in Pounds:
                <input
                type="text"
                placeholder="lbs"
                className={classes.input_field}
                value={weight_lbs}
                onChange={(e) => setWeight_lbs(e.target.value)}
                />
              </li>

              <li key={userData.age}>
                Age:
                <input
                type="text"
                placeholder="yrs"
                className={classes.input_field}
                value={age}
                onChange={(e) => setAge(e.target.value)}
                />
              </li>

              <li key={userData.height_feet}>
                Height in Feet:
                <input
                type="text"
                placeholder="ft."
                className={classes.input_field}
                value={height_feet}
                onChange={(e) => setHeight_feet(e.target.value)}
                />
              </li>

              <li key={userData.height_inches}>
                Height in Inches:
                <input
                type="text"
                placeholder="in"
                className={classes.input_field}
                value={height_inches}
                onChange={(e) => setHeight_inches(e.target.value)}
                />
              </li>

              <li key={userData.activity_level}>
                Activity Level:
                <input
                type="text"
                placeholder="low/medium/high"
                className={classes.input_field}
                value={activity_level}
                onChange={(e) => setActivity_level(e.target.value)}
                />
              </li>

              <li key={userData.vegetarian}>
                Vegetarian:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={vegetarian}
                onChange={(e) => setVegetarian(e.target.value)}
                />
              </li>

              <li key={userData.vegan}>
                Vegan:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={vegan}
                onChange={(e) => setVegan(e.target.value)}
                />
              </li>

              <li key={userData.gluten_free}>
                Gluten Free:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={gluten_free}
                onChange={(e) => setGluten_free(e.target.value)}
                />
              </li>

              <li key={userData.keto}>
                Keto:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={keto}
                onChange={(e) => setKeto(e.target.value)}
                />
              </li>

              <li key={userData.paleo}>
                Paleo:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={paleo}
                onChange={(e) => setPaleo(e.target.value)}
                />
              </li>

              <li key={userData.pescetarian}>
                Pescetarian:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={pescetarian}
                onChange={(e) => setPescetarian(e.target.value)}
                />
              </li>

              <li key={userData.preferences}>
                Preferences:
                <input
                type="text"
                placeholder="Comma seperated list"
                className={classes.input_field}
                value={preferences}
                onChange={(e) => setPreferences(e.target.value)}
                />
              </li>

              <li key={userData.restrictions}>
                Restrictions:
                <input
                type="text"
                placeholder="Comma seperated list"
                className={classes.input_field}
                value={restrictions}
                onChange={(e) => setRestrictions(e.target.value)}
                />
              </li>

              <li>
                <button type="button" className={classes.submit_button} onClick={update}>
                  Update
                </button>
              </li>     
            </ul>
        </div>
    </div>
    </div>
  );
};

export default ProfilePage;

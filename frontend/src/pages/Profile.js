import React, { useEffect, useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router-dom";
import classes from './Profile.module.css';
import { Header } from './../components/'



const ProfilePage = () => {
  const currentUser = localStorage.getItem('curruser')
  const backend = "http://localhost:5000"
  const [gender, setGender] = useState("");
  const [weight_lbs, setWeight_lbs] = useState("");
  const [age, setAge] = useState("");
  const [height_feet, setHeight_feet] = useState("");
  const [height_inches, setHeight_inches] = useState("");
  const [activity_level, setActivity_level] = useState("");
  const [vegitarian, setVegitarian] = useState("");
  const [vegan, setVegan] = useState("");
  const [halal, setHalal] = useState("");
  const [kosher, setKosher] = useState("");
  const [gluten_free, setGluten_free] = useState("");
  const [dairy_free, setDairy_free] = useState("");
  const [lactose_int, setLactose_int] = useState("");
  const [low_sodium, setLow_sodium] = useState("");
  const [low_carb, setLow_carb] = useState("");
  const [high_protein, setHigh_protein] = useState("");
  const [keto, setKeto] = useState("");
  const [paleo, setPaleo] = useState("");
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

  useEffect(async () => {
    const result = await axios.get(`${backend}/getuserinfo?user=${currentUser}`);
    setUserData(result.data.user[0]);
    setGender(result.data.user[0].gender);
    setWeight_lbs(result.data.user[0].weight_lbs);
    setAge(result.data.user[0].age);
    setHeight_feet(result.data.user[0].height_feet);
    setHeight_inches(result.data.user[0].height_inches);
    setActivity_level(result.data.user[0].activity_level);
    setVegitarian(result.data.user[0].vegitarian);
    setVegan(result.data.user[0].vegan);
    setHalal(result.data.user[0].halal);
    setKosher(result.data.user[0].kosher);
    setGluten_free(result.data.user[0].gluten_free);
    setDairy_free(result.data.user[0].dairy_free);
    setLactose_int(result.data.user[0].lactose_int);
    setLow_sodium(result.data.user[0].low_sodium)
    setLow_carb(result.data.user[0].low_carb)
    setHigh_protein(result.data.user[0].high_protein)
    setKeto(result.data.user[0].keto)
    setPaleo(result.data.user[0].paleo)
    setPreferences(result.data.user[0].preferences)
    setRestrictions(result.data.user[0].restrictions)

    // console.log("test"+ gender);
  }, []);

  const update = async () => {
    const updateData = await axios.put(`${backend}/updateuser?user=${currentUser}&gender=${gender}&weight_lbs=${weight_lbs}&age=${age}&height_feet=${height_feet}&height_inches=${height_inches}&activity_level=${activity_level}&vegitarian=${vegitarian}&vegan=${vegan}&halal=${halal}&kosher=${kosher}&gluten_free=${gluten_free}&dairy_free=${dairy_free}&lactose_int=${lactose_int}&low_sodium=${low_sodium}&low_carb=${low_carb}&high_protein=${high_protein}&keto=${keto}&paleo=${paleo}&preferences=${preferences}&restrictions=${restrictions}`)
    console.log(updateData.data)

  
};
  return (
    <div>
      <Header />
    
    <div className={classes.contained}>
      <div className={classes.form}>
        <h1>User Info Form </h1>
            <ul>
              <li key={userData.gender}>
                Gender:
                <input
                type="text"
                placeholder="Gender"
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
                Heigt in Inches:
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
                placeholder="Low/Medium/High"
                className={classes.input_field}
                value={activity_level}
                onChange={(e) => setActivity_level(e.target.value)}
                />
              </li>

              <li key={userData.vegitarian}>
                Vegitarian:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={vegitarian}
                onChange={(e) => setVegitarian(e.target.value)}
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

              <li key={userData.halal}>
                Halal:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={halal}
                onChange={(e) => setHalal(e.target.value)}
                />
              </li>

              <li key={userData.kosher}>
                Kosher:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={kosher}
                onChange={(e) => setKosher(e.target.value)}
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

              <li key={userData.dairy_free}>
                Diary Free:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={dairy_free}
                onChange={(e) => setDairy_free(e.target.value)}
                />
              </li>

              <li key={userData.lactose_int}>
                Lactose Intolerant:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={lactose_int}
                onChange={(e) => setLactose_int(e.target.value)}
                />
              </li>

              <li key={userData.low_sodium}>
                Low Sodium:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={low_sodium}
                onChange={(e) => setLow_sodium(e.target.value)}
                />
              </li>

              <li key={userData.low_carb}>
                Low Carbs:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={low_carb}
                onChange={(e) => setLow_carb(e.target.value)}
                />
              </li>

              <li key={userData.high_protein}>
                High Protein:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={high_protein}
                onChange={(e) => setHigh_protein(e.target.value)}
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

              <li key={userData.preferences}>
                Preferences:
                <input
                type="text"
                placeholder="True or False"
                className={classes.input_field}
                value={preferences}
                onChange={(e) => setPreferences(e.target.value)}
                />
              </li>

              <li key={userData.restrictions}>
                Restrictions:
                <input
                type="text"
                placeholder="True or False"
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

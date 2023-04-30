import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import './Recipes.css';
import { Header } from './../components/'
import './Style.css';


const ImageGallery = ({ imageLinks, handleImageToggle }) => {
     const [selectedImages, setSelectedImages] = useState([]);
     const navigate = useNavigate();
     const handleImageClick = (link) => {
          if (selectedImages.includes(link)) {
               setSelectedImages(selectedImages.filter((selectedLink) => selectedLink !== link));
          } else {
               setSelectedImages([...selectedImages, link]);
          }
     };

     //WeeklyRecipes
     const sendLinks = async () => {
          const backend = "http://localhost:5000";
          const idsString = selectedImages.join(',');
          const curruserID = localStorage.getItem("curruserID");
          const currweek = localStorage.getItem("currWeek");
          await axios.post(`${backend}/post_recipes/${curruserID}/${currweek}?userID=${curruserID}&recipe_string=${idsString}`)
          //await axios.post(`${backend}/post_grocery_list/${curruserID}/${currweek}`)

          navigate("/home");
          console.log(idsString);
     };
     
     return (
          <div>
               {imageLinks.map((link, index) => (
               <div key={index} className="image-container">
                    <img
                    src={link.image}
                    alt={`Image ${index + 1}`}
                    className={selectedImages.includes(link.id) ? 'image selected' : 'image'}
                    onClick={() => handleImageClick(link.id)}
                    />
                    <p>{link.title}</p>
                    <input
                    type="checkbox"
                    className="checkbox"
                    checked={selectedImages.includes(link.id)}
                    onChange={() => handleImageToggle(link.id)}
                    />
               </div>
               ))}

               <button onClick={() => sendLinks()}>
                    Submit
               </button>

          </div>
     );
};
function RecipesPage() {
     const backend = "http://localhost:5000";
     const curruserID = localStorage.getItem("curruserID");
     //const [data, setData] = useState(null);
     const [link_arr, setLink] = useState([]);

     useEffect( () => {
          const get_list = async () => {
               axios.get(`${backend}/get_recipe_list/${curruserID}`)
               //.then(response => {console.log(response.data.results);})
               .then(response => {
                    console.log(response.data.results);
                    //setData(response.data.results);
                    console.log(response);
                    const links_index = response.data.results.map(entity => {
                         return {
                              image: entity.image,
                              id: entity.id,
                              title: entity.title
                         };
                    });
                    setLink(links_index);
                    //console.log("====>>>" + links_index[0].image);
               })
               .catch(error => {
                    console.error('Error fetching data:', error);
               });
               
          };
          
          get_list();
          
     }, []);

     const handleImageToggle = (link) => {
          console.log(`Image link: ${link} toggled`);
          // Do something with the selected image link
     };
     

     return (
         
          <div style={{paddingBottom:"10vh"}} className="App" >
               <Header />
               
               <ImageGallery
               imageLinks={link_arr}
               handleImageToggle={handleImageToggle}
               />

          </div>
     );

}

export default RecipesPage;

import React, { useState, useEffect } from "react";
import axios from 'axios';
import './Recipes.css';


const ImageGallery = ({ imageLinks, handleImageToggle }) => {
     const [selectedImages, setSelectedImages] = useState([]);
   
     const handleImageClick = (link) => {
          if (selectedImages.includes(link)) {
               setSelectedImages(selectedImages.filter((selectedLink) => selectedLink !== link));
          } else {
               setSelectedImages([...selectedImages, link]);
          }
     };

     //WeeklyRecipes
     const sendLinks = async () => {
          const idsString = selectedImages.join(',');
          // const data = await axios.post(`http://127.0.0.1:5000/post_recipes/1?recipe_string=${idsString}`)
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
     const [data, setData] = useState(null);
     const [link_arr, setLink] = useState([]);
     const [link_str, setString] = useState("");

     useEffect( () => {
          const get_list = async () => {
               axios.get('http://127.0.0.1:5000/get_recipes/1')
               .then(response => {
                    setData(response.data);
                    //console.log(response.data[0].calories);
                    // setLink(response.data.map(obj => obj.image));
                    const links_index = response.data.map(entity => {
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
          <div> 
               <h1>Recipes</h1>
               <ImageGallery
               imageLinks={link_arr}
               handleImageToggle={handleImageToggle}
               />
               

          </div>
     );

}

export default RecipesPage;

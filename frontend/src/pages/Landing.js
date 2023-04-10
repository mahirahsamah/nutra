
function LandingPage() {
     
     // renderName = () => {
     //      return localStorage.getItem('nameone');
     //      // innerHtml 
     // };

     return (
          
          // <p id='namehere'> hello </p>
          <div> Hello { localStorage.getItem('curruser') }!! </div>
     );

}

export default LandingPage;
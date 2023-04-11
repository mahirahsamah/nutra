
function LandingPage() {
     
     // renderName = () => {
     //      return localStorage.getItem('nameone');
     //      // innerHtml 
     // };

     return (
          <div> Hello { localStorage.getItem('curruser') }!! </div>
     );

}

export default LandingPage;
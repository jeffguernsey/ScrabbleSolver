import React from 'react';
import Header from './Header.js'
import Forms from './Forms.js'
import Footer from './Footer.js'
//The Goal of this project is to interface with our custom API to provide all possible scrabble answers
function App(){
    return(
        <div>
          <Header/>
          <Forms/>
          <Footer/>
        </div>
      )
}
export default App;

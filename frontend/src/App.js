import React, {useState, useEffect} from 'react'
import Profile from './components/Profile'

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/dummy").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>
      {(typeof data.custom === 'undefined')? (
        <p>Loading...</p>
      ) : (
        data.custom.map((custom, i) => (
          <p key={i}>{custom}</p>
        ))
      )}

  <Profile />
    </div>
  )
}

export default App
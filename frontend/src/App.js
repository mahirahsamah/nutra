import React, {useState, useEffect} from 'react'

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
    </div>
  )
}

export default App
import { useState, useEffect } from 'react'


function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    let isRunning = true

    fetch('http://127.0.0.1:8000/wisdom')
    .then((res) => res.json())
    .then((data) => {
        console.log("What is the data?", data)
        if (isRunning) {
            setItems(data)
        }
    })

    return () => {
        isRunning = false;
    }
  }, [])

  return (
    <div>
      <h2>Wise Quotes</h2>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <h3>{item.heading}</h3>
            <blockquote><em><q>{item.aphorism}</q></em></blockquote>
            <p>~ {item.author}</p>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App

import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UploadAnnotator from './UploadAnnotator' // Add this import


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      
      <UploadAnnotator /> {/* Add this line to render the component */}
      
    </>
  )
}

export default App

import React from 'react'
import ReactDOM from 'react-dom/client'
import 'regenerator-runtime/runtime'; // Required for react-speech-recognition
import App from './App.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

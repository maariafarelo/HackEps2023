import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ReactDOM from 'react-dom/client'
import App from './App.jsx';
import Admin from './Admin.jsx';
import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <Router>
    <React.StrictMode>
      <Routes>
        <Route exact path="/" element={<App />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </React.StrictMode>
  </Router>,
);
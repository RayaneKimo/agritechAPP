import React from "react";
import { createRoot } from "react-dom/client";
import Dashboard from "./Dashboard";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./index.css";

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/dashboard">Dashboard</Link>
            </li>
          </ul>
        </nav>

        
        <Routes>
          
          <Route path='/dashboard' element={<Dashboard/>} />
          <Route path='/' element={<div>You are in home</div>} />

        </Routes>
      </div>
    </Router>
  );
};

createRoot(document.getElementById("root")).render(<App />);

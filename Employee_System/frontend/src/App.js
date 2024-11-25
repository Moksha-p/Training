import React, { useState } from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from './components/Home';

import DepartmentList from './components/departments/DepartmentList';
import EmployeeList from './components/employees/EmployeeList';
import ProjectList from './components/projects/ProjectList';
import 'bootstrap/dist/css/bootstrap.min.css';
import SubmitButton from './components/SubmitButton';
import { Button } from "react-bootstrap";

function App() {
  const [category, setCategory] = useState  ("");

  const handleCategoryChange = (newCategory) => {
    setCategory(newCategory);
  };
    return (
        <Router>
            <Navbar />
            <div className="container mt-4">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/departments" element={<DepartmentList />} />
                    <Route path="/employees" element={<EmployeeList />} />
                    <Route path="/projects" element={<ProjectList />} />
                </Routes>
            </div>
            
        </Router>
    );
}

export default App;

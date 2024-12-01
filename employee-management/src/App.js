import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import EmployeeTable from './components/EmployeeTable';
import ProjectTable from './components/ProjectTable';
import DepartmentTable from './components/DepartmentTable';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Employees</Link></li>
          <li><Link to="/projects">Projects</Link></li>
          <li><Link to="/departments">Departments</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<EmployeeTable />} />
        <Route path="/projects" element={<ProjectTable />} />
        <Route path="/departments" element={<DepartmentTable />} />
      </Routes>
    </Router>
  );
}

export default App;

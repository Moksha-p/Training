import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import EmployeeTable from './components/EmployeeTable';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<EmployeeTable />} />
      </Routes>
    </Router>
  );
}

export default App;

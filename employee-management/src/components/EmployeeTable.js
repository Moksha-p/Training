import React, { useState, useEffect } from 'react';
import axios from 'axios';

const EmployeeTable = () => {
  const [employees, setEmployees] = useState([]); // State for employee data
  const [loading, setLoading] = useState(true);  // State for loading indicator

  // Fetch data from the backend API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/employees/') // Update this URL with your backend API
      .then(response => {
        setEmployees(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching employees:', error);
        setLoading(false);
      });
  }, []);

  // Conditional rendering: show loading message while fetching data
  if (loading) {
    return <p>Loading employee data...</p>;
  }

  // Render employee data in a table
  return (
    <div>
      <h1>Employee List</h1>
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Salary</th>
            <th>Designation</th>
            <th>Department</th>
            <th>Address</th>
          </tr>
        </thead>
        <tbody>
          {employees.map(employee => (
            <tr key={employee.id}>
              <td>{employee.id}</td>
              <td>{employee.name}</td>
              <td>{employee.salary}</td>
              <td>{employee.designation}</td>
              <td>{employee.department?.name || 'N/A'}</td>
              <td>{employee.address}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default EmployeeTable;

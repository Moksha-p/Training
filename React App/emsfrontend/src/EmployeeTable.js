import React from 'react';

const EmployeeTable = ({ employees }) => {
    return  (
        <div>
            <h1>Employees</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Salary</th>
                        <th>Designation</th>
                        <th>Department</th>
                        <th>Address</th>
                        <th>Projects</th>
                    </tr>
                </thead>
                <tbody>
                    {employees.map(employee => (
                      <tr>
                          <td>{employee.id}</td>
                          <td>{employee.name}</td>
                          <td>{employee.salary}</td>
                          <td>{employee.designation}</td>
                          <td>{employee.department}</td>
                          <td>{employee.address}</td>
                          <td>{employee.projects}</td>
                      </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default EmployeeTable;
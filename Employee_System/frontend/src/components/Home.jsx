import React from 'react';
import EmployeeList from './employees/EmployeeList';
import DepartmentList from './departments/DepartmentList';
import ProjectsList from './projects/ProjectList';

const Home = () => {
  return (
    <div style={{ margin: '20px' }}>
      {/* Employee Section */}
      <div style={{ marginBottom: '40px' }}>
        <h2 className='center'>Employee List</h2>
        <EmployeeList />
      </div>

      {/* Department Section */}
      <div style={{ marginBottom: '40px' }}>
        <h2>Department List</h2>
        <DepartmentList />
      </div>

      {/* Projects Section */}
      <div>
        <h2>Projects List</h2>
        <ProjectsList />
      </div>
    </div>
  );
};

export default Home;

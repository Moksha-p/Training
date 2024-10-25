import React from 'react';

const DepartmentTable = ({ departments }) => {
    return  (
        <div>
            <h1>Departments</h1>
               <table>
                   <thead>
                       <tr>
                           <th>ID</th>
                           <th>Name</th>
                       </tr>
                   </thead>
                   <tbody>
                       {departments.map(department => (
                        <tr>
                            <td>{department.id}</td>
                            <td>{department.name}</td>
                        </tr>
                      ))}
                  </tbody>
              </table>
        </div>
    );
};

export default DepartmentTable;
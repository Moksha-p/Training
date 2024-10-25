import React from "react";

const ProjectTable = ({ projects }) => {
    return (
        <div>
            <h1>Projects</h1>
              <table>
                  <thead>
                      <tr>
                          <th>ID</th>
                          <th>Team</th>
                          <th>Name</th>
                          <th>Status</th>
                          <th>Start Date</th>
                          <th>End Date</th>
                          <th>Team Lead</th>
                      </tr>
                  </thead>
                  <tbody>
                      {projects.map(project => (
                        <tr>
                            <td>{project.id}</td>
                            <td>{project.team}</td>
                            <td>{project.name}</td>
                            <td>{project.status}</td>
                            <td>{project.start_date}</td>
                            <td>{project.end_date}</td>
                            <td>{project.team_lead}</td>
                        </tr>
                      ))}
                  </tbody>
              </table>
        </div>
    );
};

export default ProjectTable;
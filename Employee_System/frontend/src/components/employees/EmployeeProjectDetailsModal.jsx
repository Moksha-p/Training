import React, { useEffect, useState } from 'react';
import { Modal, Table } from 'react-bootstrap';
import axios from 'axios';
import { toast, ToastContainer } from 'react-toastify';  // Import Toastify
import 'react-toastify/dist/ReactToastify.css';  // Import Toastify CSS

const EmployeeProjectDetailsModal = ({ show, handleClose, projectIds }) => {
  const [projects, setProjects] = useState([]);
  const [isInitialRender, setIsInitialRender] = useState(true); // Flag to check initial render

  useEffect(() => {
   
    // If there are projects, fetch them
    const fetchProjects = async () => {
      try {
        const projectPromises = projectIds.map((id) =>
          axios.get(`http://127.0.0.1:8000/api/projects/${id}/`)
        );
        const projectResponses = await Promise.all(projectPromises);
        setProjects(projectResponses.map((res) => res.data));
      } catch (error) {
        console.error('Error fetching projects:', error);
      }
    };

    fetchProjects();
  }, [projectIds, isInitialRender]);  // Depend on projectIds and initial render
  

  return (
    <>
      {/* Toastify Container for displaying toasts */}
      <ToastContainer />

      <Modal show={show} onHide={handleClose} centered>
        <Modal.Header closeButton>
          <Modal.Title>Employee's Projects</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Table striped bordered hover>
            <thead>
              <tr>
                <th>Project Name</th>
                <th>Status</th>
                <th>Start Date</th>
                <th>End Date</th>
              </tr>
            </thead>
            <tbody>
              {projects.length > 0 ? (
                projects.map((project) => (
                  <tr key={project.id}>
                    <td>{project.name}</td>
                    <td>{project.status}</td>
                    <td>{project.start_date}</td>
                    <td>{project.end_date}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="4" className="text-center">
                    No projects assigned
                  </td>
                  {}
                </tr>
              )}
            </tbody>
          </Table>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default EmployeeProjectDetailsModal;

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table';
import { Button, Modal, Form } from 'react-bootstrap';
import { FaPlus } from 'react-icons/fa';
import UpdateStatusButton from './UpdateStatusButton';
import DeleteProjectButton from './DeleteProjectButton';

const ProjectList = () => {
  const [projects, setProject] = useState([]);
  const [employees, setEmployees] = useState([]);

  const [showModal, setShowModal] = useState(false);

  // Get today's date in "YYYY-MM-DD" format
  const today = new Date().toISOString().split('T')[0];

  const [newProject, setNewProject] = useState({
    name: '',
    team: [],
    team_lead: 1,
    status: 'NEW',
    start_date: today,
    end_date: today,
  });

  // Fetch projects
  const fetchProjects = () => {
    axios
      .get('http://127.0.0.1:8000/api/projects/')
      .then((res) => setProject(res.data))
      .catch((err) => console.error('Error fetching projects:', err));
  };

  useEffect(() => {
    fetchProjects(); // Fetch projects on component mount
  }, []);

  // Fetch employees
  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/employees/')
      .then((res) => setEmployees(res.data))
      .catch((err) => console.error('Error fetching employees:', err));
  }, []);

  // Get employee name by ID
  const getEmployeeNameById = (id) => {
    const employee = employees.find((emp) => emp.id === id);
    return employee ? employee.name : 'Unknown';
  };

  // Get team member names
  const getTeamNames = (teamIds) => {
    return teamIds.map((id) => getEmployeeNameById(id)).join(', ');
  };

  // Handle modal close and reset form
  const handleCloseModal = () => {
    setShowModal(false);
    setNewProject({
      name: '',
      team: [],
      team_lead: 1,
      status: 'NEW',
      start_date: today,
      end_date: today,
    });
  };

  // Handle input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewProject({
      ...newProject,
      [name]: name === 'team' ? value.split(',').map((id) => id.trim()) : value,
    });
  };

  // Add new project
  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .post('http://127.0.0.1:8000/api/projects/', newProject)
      .then(() => {
        alert('Project added successfully!');
        fetchProjects(); // Re-fetch projects to update the list
        handleCloseModal(); // Close modal after success
      })
      .catch((error) => console.error('Error adding project:', error));
  };

  // Get status color
  const getStatusColor = (status) => {
    if (status === 'NEW') return 'green';
    if (status === 'ENDED') return 'red';
    return 'blue';
  };

  // Sort projects by ID
  const sortedProjects = [...projects].sort((a, b) => a.id - b.id);

  return (
    <div>
      {/* Add Project Button */}
      <Button
        variant="primary"
        onClick={() => setShowModal(true)}
        className="mb-4"
        style={{ display: 'flex', alignItems: 'center' }}
      >
        <FaPlus style={{ marginRight: '8px' }} />
        Add Project
      </Button>

      {/* Projects Table */}
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Project ID</th>
            <th>Project Name</th>
            <th>Project Lead</th>
            <th>Assigned Team Members</th>
            <th>Status</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {sortedProjects.map((project) => (
            <tr key={project.id}>
              <td>{project.id}</td>
              <td>{project.name}</td>
              <td>{getEmployeeNameById(project.team_lead)}</td>
              <td>{getTeamNames(project.team)}</td>
              <td style={{ color: getStatusColor(project.status) }}>
                {project.status}
              </td>
              <td>{project.start_date}</td>
              <td>{project.end_date}</td>
              <td>
                <div
                  style={{ display: 'flex', alignItems: 'center', gap: '10px' }}
                >
                  <UpdateStatusButton
                    projectId={project.id}
                    currentStatus={project.status}
                    onStatusUpdated={fetchProjects}
                  />
                  <DeleteProjectButton
                    projectId={project.id}
                    onDelete={fetchProjects}
                  />
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>

      {/* Modal for Add Project */}
      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>Add New Project</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            {/* Project Name */}
            <Form.Group controlId="name">
              <Form.Label>Project Name</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter project name"
                name="name"
                value={newProject.name}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            {/* Team Members */}
            <Form.Group controlId="team">
              <Form.Label>Team Members (Comma-separated IDs)</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter team member IDs"
                name="team"
                value={newProject.team.join(', ')}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            {/* Team Lead */}
            <Form.Group controlId="team_lead">
              <Form.Label>Team Lead ID</Form.Label>
              <Form.Control
                type="number"
                placeholder="Enter team lead ID"
                name="team_lead"
                value={newProject.team_lead}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            {/* Status */}
            <Form.Group controlId="status">
              <Form.Label>Status</Form.Label>
              <Form.Control
                as="select"
                name="status"
                value={newProject.status}
                onChange={handleInputChange}
                required
              >
                <option value="NEW">NEW</option>
                <option value="ON-GOING">IN PROGRESS</option>
                <option value="ENDED">COMPLETED</option>
              </Form.Control>
            </Form.Group>

            {/* Start Date */}
            <Form.Group controlId="start_date">
              <Form.Label>Start Date</Form.Label>
              <Form.Control
                type="date"
                name="start_date"
                value={newProject.start_date}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            {/* End Date */}
            <Form.Group controlId="end_date">
              <Form.Label>End Date</Form.Label>
              <Form.Control
                type="date"
                name="end_date"
                value={newProject.end_date}
                onChange={handleInputChange}
                required
              />
            </Form.Group>

            {/* Submit Button */}
            <Button variant="primary" type="submit" className="mt-3">
              Add Project
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </div>
  );
};

export default ProjectList;

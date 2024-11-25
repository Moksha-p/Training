import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table';
import { Button, Modal, Form } from 'react-bootstrap';
import { FaPlus } from 'react-icons/fa';
import UpdateDepartmentButton from './UpdateDepartmentButton';
import DeleteDepartmentButton from './DeleteDepartmentButton';

const DepartmentList = () => {
  const [departments, setDepartments] = useState([]);
  const [showModal, setShowModal] = useState(false); // State for controlling the modal visibility
  const [newDepartmentName, setNewDepartmentName] = useState(''); // State for new department name

  // Fetch department data from the API
  const fetchDepartments = () => {
    axios
      .get('http://127.0.0.1:8000/api/departments/')
      .then((res) => setDepartments(res.data))
      .catch((err) => console.error('Error fetching departments:', err));
  };

  useEffect(() => {
    fetchDepartments(); // Fetch departments on component mount
  }, []);
  useEffect(() => {
    fetchDepartments(); // Fetch departments on component mount
  }, []);

  // Handle modal close and reset the form
  const handleCloseModal = () => {
    setShowModal(false);
    setNewDepartmentName(''); // Reset department name
  };

  // Handle input change for new department name
  const handleDepartmentInputChange = (e) => {
    setNewDepartmentName(e.target.value);
  };

  // Handle form submission to add a new department
  const handleAddDepartment = (e) => {
    e.preventDefault();
    axios
      .post('http://127.0.0.1:8000/api/departments/', { name: newDepartmentName })
      .then(() => {
        alert('Department added successfully!');
        fetchDepartments(); // Refresh the department list
        handleCloseModal(); // Close the modal after adding
      })
      .catch((error) => console.error('Error adding department:', error));
  };

  return (
    <div>
      {/* Add Department Button */}
      <Button
        variant="primary"
        onClick={() => setShowModal(true)}
        className="mb-4"
        style={{ display: 'flex', alignItems: 'center' }}
      >
        <FaPlus style={{ marginRight: '8px' }} />
        Add Department
      </Button>

      {/* Department List Table */}
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Department ID</th>
            <th>Department Name</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {departments.map((department) => (
            <tr key={department.id}>
              <td>{department.id}</td>
              <td>{department.name}</td>
              <td>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px', justifyContent: 'center' }}>
                  {/* Update Button */}
                  <UpdateDepartmentButton
                    departmentId={department.id}
                    currentData={department}
                    onUpdate={fetchDepartments}
                  />
                  {/* Delete Button */}
                  <DeleteDepartmentButton
                    departmentId={department.id}
                    onDelete={fetchDepartments}
                  />
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </Table>

      {/* Modal for Adding Department */}
      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>Add New Department</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleAddDepartment}>
            {/* Department Name */}
            <Form.Group controlId="name">
              <Form.Label>Department Name</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter department name"
                value={newDepartmentName}
                onChange={handleDepartmentInputChange}
                required
              />
            </Form.Group>

            {/* Submit Button */}
            <Button variant="primary" type="submit" className="mt-3">
              Add Department
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </div>
  );
};

export default DepartmentList;

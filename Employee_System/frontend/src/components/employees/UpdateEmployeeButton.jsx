import React, { useState } from 'react';
import { Button, Modal, Form } from 'react-bootstrap';
import axios from 'axios';

const UpdateEmployeeButton = ({ employeeId, currentData, onUpdate }) => {
  const [showModal, setShowModal] = useState(false);
  const [updatedEmployee, setUpdatedEmployee] = useState(currentData);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUpdatedEmployee({ ...updatedEmployee, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .put(`http://127.0.0.1:8000/api/employees/${employeeId}/`, updatedEmployee)
      .then(() => {
        alert('Employee updated successfully!');
        onUpdate(); // Refresh the employee list
        setShowModal(false); // Close the modal
      })
      .catch((error) => console.error('Error updating employee:', error));
  };

  return (
    <>
      <Button variant="warning" onClick={() => setShowModal(true)}>
        Update
      </Button>
      <Modal show={showModal} onHide={() => setShowModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Update Employee</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="name">
              <Form.Label>Full Name</Form.Label>
              <Form.Control
                type="text"
                name="name"
                value={updatedEmployee.name}
                onChange={handleInputChange}
                required
              />
            </Form.Group>
            <Form.Group controlId="salary">
              <Form.Label>Salary</Form.Label>
              <Form.Control
                type="number"
                name="salary"
                value={updatedEmployee.salary}
                onChange={handleInputChange}
                required
              />
            </Form.Group>
            <Form.Group controlId="designation">
              <Form.Label>Designation</Form.Label>
              <Form.Control
                type="text"
                name="designation"
                value={updatedEmployee.designation}
                onChange={handleInputChange}
                required
              />
            </Form.Group>
            <Button variant="primary" type="submit">
              Update
            </Button>
          </Form>
        </Modal.Body>
      </Modal>
    </>
  );
};

export default UpdateEmployeeButton;

import React, { useState } from 'react';
import { Button, Modal, Form } from 'react-bootstrap';
import axios from 'axios';

const UpdateDepartmentButton = ({ departmentId, currentData, onUpdate }) => {
  const [showModal, setShowModal] = useState(false);
  const [updatedDepartment, setUpdatedDepartment] = useState(currentData);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUpdatedDepartment({ ...updatedDepartment, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .put(`http://127.0.0.1:8000/api/departments/${departmentId}/`, updatedDepartment)
      .then(() => {
        alert('Department updated successfully!');
        onUpdate();
        setShowModal(false);
      })
      .catch((error) => console.error('Error updating department:', error));
  };

  return (
    <>
      <Button variant="warning" onClick={() => setShowModal(true)}>
        Update
      </Button>
      <Modal show={showModal} onHide={() => setShowModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>Update Department</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="name">
              <Form.Label>Department Name</Form.Label>
              <Form.Control
                type="text"
                name="name"
                value={updatedDepartment.name}
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

export default UpdateDepartmentButton;

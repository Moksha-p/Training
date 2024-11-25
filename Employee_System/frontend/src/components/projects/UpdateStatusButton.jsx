import React, { useState } from 'react';
import axios from 'axios';
import { Button, Modal, Form } from 'react-bootstrap';
import { FaEdit, FaTrash } from 'react-icons/fa';

const UpdateStatusButton = ({ projectId, currentStatus, onStatusUpdated  }) => {
  const [showModal, setShowModal] = useState(false);
  const [newStatus, setNewStatus] = useState(currentStatus);

  // Function to toggle modal visibility
  const toggleModal = () => setShowModal(!showModal);

  // Function to handle status update
  const handleUpdateStatus = () => {
    axios.put(`http://127.0.0.1:8000/api/projects/${projectId}/`, {
      status: newStatus,
    })
      .then(response => {
        alert('Status updated successfully');
        toggleModal(); // Close the modal
        onStatusUpdated();
      })
      .catch(error => {
        console.log(projectId)
        console.log(currentStatus)
        if (error.response) {
            // The request was made, but the server responded with an error status
            console.error('Error response:', error.response.data);
            alert(`Error: ${error.response.data.detail || error.response.data}`);
          } else if (error.request) {
            // The request was made but no response was received
            console.error('Error request:', error.request);
            alert('No response received from the server.');
          } else {
            // Something else happened
            console.error('Error message:', error.message);
            alert('An error occurred while updating the project status.');
          }
        
      });
  };

  return (
    <>
      <Button variant="warning" onClick={toggleModal}>
      <FaEdit />
      </Button>

      {/* Modal for updating status */}
      <Modal show={showModal} onHide={toggleModal}>
        <Modal.Header closeButton>
          <Modal.Title>Update Project Status</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Group controlId="status">
              <Form.Label>Status</Form.Label>
              <Form.Control
                as="select"
                value={newStatus}
                onChange={(e) => setNewStatus(e.target.value)}
              >
                <option value="NEW">NEW</option>
                <option value="ON-GOING">IN PROGRESS</option>
                <option value="ENDED">COMPLETED</option>
              </Form.Control>
            </Form.Group>
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={toggleModal}>
            Close
          </Button>
          <Button variant="primary" onClick={handleUpdateStatus}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
};

export default UpdateStatusButton;

import React from 'react';
import { Button } from 'react-bootstrap';
import axios from 'axios';

const DeleteEmployeeButton = ({ employeeId, onDelete }) => {
  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this employee?')) {
      axios
        .delete(`http://127.0.0.1:8000/api/employees/${employeeId}/`)
        .then(() => {
          alert('Employee deleted successfully!');
          onDelete(); // Refresh the employee list
        })
        .catch((error) => console.error('Error deleting employee:', error));
    }
  };

  return (
    <Button variant="danger" onClick={handleDelete}>
      Delete
    </Button>
  );
};

export default DeleteEmployeeButton;

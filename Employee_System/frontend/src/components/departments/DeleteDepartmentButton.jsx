import React from 'react';
import { Button } from 'react-bootstrap';
import axios from 'axios';

const DeleteDepartmentButton = ({ departmentId, onDelete }) => {
  const handleDelete = () => {
    if (window.confirm('Are you sure you want to delete this department?')) {
      axios
        .delete(`http://127.0.0.1:8000/api/departments/${departmentId}/`)
        .then(() => {
          alert('Department deleted successfully!');
          onDelete();
        })
        .catch((error) => console.error('Error deleting department:', error));
    }
  };

  return (
    <Button variant="danger" onClick={handleDelete}>
      Delete
    </Button>
  );
};

export default DeleteDepartmentButton;

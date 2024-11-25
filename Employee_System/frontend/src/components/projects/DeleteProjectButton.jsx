import React from 'react';
import axios from 'axios';
import { Button } from 'react-bootstrap';
import { FaEdit, FaTrash } from 'react-icons/fa';

const DeleteProjectButton = ({ projectId, onDelete }) => {
  const handleDeleteProject = () => {
    
      axios.delete(`http://127.0.0.1:8000/api/projects/${projectId}/`)
        .then(response => {
            if(response.data.error){
                alert('Project cannot be delete before it"s End date')
            }else{
                alert('Project deleted successfully');
                onDelete();
            }
        })
        .catch(error => {
          console.error('Error deleting project:', error);
          alert('Failed to delete project');
        });
    
  };

  return (
    <Button variant="danger" onClick={handleDeleteProject}>
      <FaTrash /> 
    </Button>
  );
};

export default DeleteProjectButton;

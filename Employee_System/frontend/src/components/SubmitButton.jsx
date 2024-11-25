import React, { useState } from 'react';
import axios from 'axios';
import { Button, Form } from 'react-bootstrap';

const SubmitButton = ({ category }) => {
  const [formData, setFormData] = useState({
    name: '',
    salary: '',
    designation: '',
    department: '',
    address: '',
    projects: [],
    team: [],
    team_lead: '',
    status: '',
    start_date: '',
    end_date: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    let apiUrl = "";
    let dataToSend = {};

    if (category === "employee") {
      apiUrl = "http://127.0.0.1:8000/api/employees/";
      dataToSend = {
        name: formData.name,
        salary: formData.salary,
        designation: formData.designation,
        department: formData.department,
        address: formData.address,
        projects: formData.projects.split(","),
      };
    } else if (category === "department") {
      apiUrl = "http://127.0.0.1:8000/api/departments/";
      dataToSend = {
        name: formData.name,
      };
    } else if (category === "project") {
      apiUrl = "http://127.0.0.1:8000/api/projects/";
      dataToSend = {
        name: formData.name,
        team: formData.team.split(","),
        team_lead: formData.team_lead,
        status: formData.status,
        start_date: formData.start_date,
        end_date: formData.end_date,
      };
    }

    try {
      await axios.post(apiUrl, dataToSend);
      alert(`${category.charAt(0).toUpperCase() + category.slice(1)} added successfully!`);
    } catch (error) {
      console.error("Error adding data", error);
      alert("Error adding data");
    }
  };

  return (
    <div>
      <h2>Add {category.charAt(0).toUpperCase() + category.slice(1)}</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="formName">
          <Form.Label>Name</Form.Label>
          <Form.Control
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            placeholder={`Enter ${category === 'employee' ? 'employee' : category} name`}
            required
          />
        </Form.Group>

        {category === "employee" && (
          <>
            <Form.Group controlId="formSalary">
              <Form.Label>Salary</Form.Label>
              <Form.Control
                type="number"
                name="salary"
                value={formData.salary}
                onChange={handleChange}
                placeholder="Enter salary"
                required
              />
            </Form.Group>

            <Form.Group controlId="formDesignation">
              <Form.Label>Designation</Form.Label>
              <Form.Control
                type="text"
                name="designation"
                value={formData.designation}
                onChange={handleChange}
                placeholder="Enter designation"
                required
              />
            </Form.Group>

            <Form.Group controlId="formDepartment">
              <Form.Label>Department ID</Form.Label>
              <Form.Control
                type="number"
                name="department"
                value={formData.department}
                onChange={handleChange}
                placeholder="Enter department ID"
                required
              />
            </Form.Group>
            <Form.Group controlId="formAddress">
              <Form.Label>Address</Form.Label>
              <Form.Control
                type="text"
                name="address"
                value={formData.address}
                onChange={handleChange}
                placeholder="Enter address"
                required
              />
            </Form.Group>
          </>
        )}

        {category === "project" && (
          <>
            <Form.Group controlId="formTeam">
              <Form.Label>Team (comma-separated IDs)</Form.Label>
              <Form.Control
                type="text"
                name="team"
                value={formData.team}
                onChange={handleChange}
                placeholder="Enter team member IDs"
              />
            </Form.Group>

            <Form.Group controlId="formTeamLead">
              <Form.Label>Team Lead ID</Form.Label>
              <Form.Control
                type="number"
                name="team_lead"
                value={formData.team_lead}
                onChange={handleChange}
                placeholder="Enter team lead ID"
              />
            </Form.Group>

            <Form.Group controlId="formStatus">
              <Form.Label>Status</Form.Label>
              <Form.Control
                type="text"
                name="status"
                value={formData.status}
                onChange={handleChange}
                placeholder="Enter project status"
              />
            </Form.Group>

            <Form.Group controlId="formStartDate">
              <Form.Label>Start Date</Form.Label>
              <Form.Control
                type="date"
                name="start_date"
                value={formData.start_date}
                onChange={handleChange}
                placeholder="Enter start date"
              />
            </Form.Group>

            <Form.Group controlId="formEndDate">
              <Form.Label>End Date</Form.Label>
              <Form.Control
                type="date"
                name="end_date"
                value={formData.end_date}
                onChange={handleChange}
                placeholder="Enter end date"
              />
            </Form.Group>
          </>
        )}

        <Button variant="primary" type="submit">
          Add {category.charAt(0).toUpperCase() + category.slice(1)}
        </Button>
      </Form>
    </div>
  );
};

export default SubmitButton;

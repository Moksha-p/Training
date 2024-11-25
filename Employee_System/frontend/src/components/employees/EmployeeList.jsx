import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Table from 'react-bootstrap/Table';
import { Button, Modal, Form } from 'react-bootstrap';
import { FaPlus, FaArrowUp, FaArrowDown } from 'react-icons/fa';
import UpdateEmployeeButton from './UpdateEmployeeButton';
import DeleteEmployeeButton from './DeleteEmployeeButton ';
import EmployeeProjectDetailsModal from './EmployeeProjectDetailsModal';

const EmployeeList = () => {
    const [employees, setEmployees] = useState([]);
    const [showModal, setShowModal] = useState(false); // State for controlling the modal visibility
    const [sortOrder, setSortOrder] = useState('asc'); // 'asc' for ascending, 'desc' for descending

    const [newEmployee, setNewEmployee] = useState({
        name: '',
        salary: '',
        designation: '',
        department: 1, // default department ID
        address: '',
        projects: [],
    });

    const [showProjectModal, setShowProjectModal] = useState(false);
    const [selectedEmployeeProjects, setSelectedEmployeeProjects] = useState([]);

    // Fetch employee data from the API
    const fetchEmployees = () => {
        axios
            .get('http://127.0.0.1:8000/api/employees/')
            .then((res) => {
                const sortedEmployees = res.data.sort((a, b) => a.id - b.id); // Sort by ID
                setEmployees(sortedEmployees);
            })
            .catch((err) => console.error('Error fetching employees:', err));
    };

    useEffect(() => {
        fetchEmployees();
    }, []);

    // Handle modal close and reset the form
    const handleCloseModal = () => {
        setShowModal(false);
        setNewEmployee({
            name: '',
            salary: '',
            designation: '',
            department: 1,
            address: '',
            projects: [],
        });
    };

    const handleDoubleClickSort = () => {
        // When double-clicked, sort by ID
        const sortedById = [...employees].sort((a, b) => a.id - b.id);
        setEmployees(sortedById); // Update state with ID sorted employees
        setSortOrder(''); // Reset sortOrder to indicate sorting by ID
    };

    // Handle input change in the form
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewEmployee({
            ...newEmployee,
            [name]: value,
        });
    };

    const handleEmployeeClick = (employee) => {
        setSelectedEmployeeProjects(employee.projects); // Get the list of project IDs
        setShowProjectModal(true); // Show the modal
    };

    // Close the project details modal
    const handleCloseProjectModal = () => {
        setShowProjectModal(false); // Hide the modal
    };

    // Handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();

        axios.post('http://127.0.0.1:8000/api/employees/', newEmployee)
            .then(res => {

                setEmployees([...employees, res.data]); // Update the employee list with the newly added employee
                handleCloseModal(); // Close the modal after submission
            })
            .catch(error => {
                console.error('There was an error adding the employee!', error);
            });
    };

    // Handle sorting employees by salary
    const handleSort = () => {
        const sortedEmployees = [...employees].sort((a, b) => {
            if (sortOrder === 'asc') {
                return a.salary - b.salary; // Ascending order
            } else {
                return b.salary - a.salary; // Descending order
            }
        });

        setEmployees(sortedEmployees); // Update the employees state with sorted data

        // Toggle sorting order for next click
        setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    };

    return (
        <div>
            {/* Add Employee Button */}
            <div className="" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <Button
                    variant="primary"
                    onClick={() => setShowModal(true)}
                    className="mb-4"
                    style={{ display: 'flex', alignItems: 'center' }} // Button style
                >
                    <FaPlus style={{ marginRight: '8px' }} /> {/* Icon with some margin */}
                    Add Employee
                </Button>

                <Button
                    variant="primary"
                    onClick={handleSort}
                    onDoubleClick={handleDoubleClickSort}
                    className="mb-4"
                    style={{ display: 'flex', alignItems: 'center' }} // Button style
                >
                    {sortOrder === 'asc' ? (
                        <FaArrowUp style={{ marginRight: '8px' }} />
                    ) : (
                        <FaArrowDown style={{ marginRight: '8px' }} />
                    )}
                    Sort By Salary
                </Button>
            </div>

            {/* Employee List Table */}
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Emp ID.</th>
                        <th>Full Name</th>
                        <th>Salary</th>
                        <th>Designation</th>
                        <th>Address</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {employees.map((employee) => (
                        <tr key={employee.id} onDoubleClick={() => handleEmployeeClick(employee)}>
                            <td>{employee.id}</td>
                            <td>{employee.name}</td>
                            <td>{employee.salary}</td>
                            <td>{employee.designation}</td>
                            <td>{employee.address}</td>
                            <td>
                                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '10px' }}>
                                    <UpdateEmployeeButton
                                        employeeId={employee.id}
                                        currentData={employee}
                                        onUpdate={fetchEmployees}
                                    />
                                    <DeleteEmployeeButton
                                        employeeId={employee.id}
                                        onDelete={fetchEmployees}
                                    />
                                </div>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </Table>
            <EmployeeProjectDetailsModal
                show={showProjectModal}
                handleClose={handleCloseProjectModal}
                projectIds={selectedEmployeeProjects}
            />
            {/* Modal for Add Employee Form */}
            <Modal show={showModal} onHide={handleCloseModal}>
                <Modal.Header closeButton>
                    <Modal.Title>Add New Employee</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <Form onSubmit={handleSubmit}>
                        {/* Name */}
                        <Form.Group controlId="name">
                            <Form.Label>Full Name</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="Enter name"
                                name="name"
                                value={newEmployee.name}
                                onChange={handleInputChange}
                                required
                            />
                        </Form.Group>

                        {/* Salary */}
                        <Form.Group controlId="salary">
                            <Form.Label>Salary</Form.Label>
                            <Form.Control
                                type="number"
                                placeholder="Enter salary"
                                name="salary"
                                value={newEmployee.salary}
                                onChange={handleInputChange}
                                required
                            />
                        </Form.Group>

                        {/* Designation */}
                        <Form.Group controlId="designation">
                            <Form.Label>Designation</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="Enter designation"
                                name="designation"
                                value={newEmployee.designation}
                                onChange={handleInputChange}
                                required
                            />
                        </Form.Group>

                        {/* Department */}
                        <Form.Group controlId="department">
                            <Form.Label>Department ID</Form.Label>
                            <Form.Control
                                type="number"
                                placeholder="Enter department ID"
                                name="department"
                                value={newEmployee.department}
                                onChange={handleInputChange}
                                required
                            />
                        </Form.Group>

                        {/* Address */}
                        <Form.Group controlId="address">
                            <Form.Label>Address</Form.Label>
                            <Form.Control
                                type="text"
                                placeholder="Enter address"
                                name="address"
                                value={newEmployee.address}
                                onChange={handleInputChange}
                                required
                            />
                        </Form.Group>

                        {/* Submit Button */}
                        <Button variant="primary" type="submit" className="mt-3">
                            Submit
                        </Button>
                    </Form>
                </Modal.Body>
            </Modal>
        </div>
    );
};

export default EmployeeList;

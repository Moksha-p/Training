import React from 'react';
import { Link } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav'; // To group navigation links

const NavbarComponent = () => {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container>
        <Navbar.Brand href="/">Employee Management System(EMS)</Navbar.Brand>
        <Nav className="ml-auto">
          {/* Add links to different pages */}
          <Nav.Link as={Link} to="/employees">Employees</Nav.Link>
          <Nav.Link as={Link} to="/departments">Departments</Nav.Link>
          <Nav.Link as={Link} to="/projects">Projects</Nav.Link>
          {/* Add more links for other paths as needed */}
        </Nav>
      </Container>
    </Navbar>
  );
};

export default NavbarComponent;

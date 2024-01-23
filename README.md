# Employee-Management-System
This Wen page help to manage Employee Status
# Employee Management System

This is a simple Employee Management System implemented using Django, a high-level web framework for Python.

## Features

- **Employee Module:**
  - Admin page for CRUD operations on Employee.
  - Display employee hierarchy within each department.

- **Department Module:**
  - Admin page for CRUD operations on Departments.
  - Display employee hierarchy for each department.
  - Ensure a department always has one manager on top and can have multiple TLs and associates.

- **Salary Module:**
  - Admin page for CRUD operations on Employee Salary entries.
  - Validate that salary entries do not overlap for the same employee.

## Project Structure

The project is structured as follows:

- **employee_management/:**
  - Main project folder.

- **employee_management/employee/:**
  - App for Employee module.

- **employee_management/department/:**
  - App for Department module.

- **employee_management/salary/:**
  - App for Salary module.




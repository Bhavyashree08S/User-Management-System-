# User Management System using Python, Streamlit, and MySQL

## Overview

The User Management System is a database-driven web application developed using Python, Streamlit, and MySQL. The application provides a secure and interactive platform for user registration, authentication, account management, and account deletion. It implements complete CRUD (Create, Read, Update, Delete) operations while ensuring data validation and reliable database interactions.

This project demonstrates the practical application of database connectivity, user authentication, input validation, SQL query execution, and modular programming concepts.

## Features

* User registration with unique username validation
* Strong password validation based on security requirements
* Secure login authentication
* User-friendly error handling and validation messages
* Update account information, including username and password
* Delete account with confirmation prompt
* Persistent data storage using MySQL
* Interactive web interface built with Streamlit
* Modular and maintainable code structure

## Technologies Used

* Python
* Streamlit
* MySQL
* SQL Queries
* Regular Expressions (Regex)
* CRUD Operations
* Modular Programming

## Project Structure

```text
User-Management-System
│
├── Home.py
├── db.py
├── validation.py
├── requirements.txt
├── README.md
│
└── pages
    ├── signup.py
    ├── login.py
    └── welcome.py
```

## Database Setup

### Create Database

```sql
CREATE DATABASE UMS;
USE UMS;
```

### Create Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### Configure Database Connection

Update the database credentials in `db.py` before running the application:

```python
host="localhost"
user="YOUR_USERNAME"
password="YOUR_PASSWORD"
database="UMS"
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Launch the Streamlit application using:

```bash
streamlit run Home.py
```

## Validation Rules

### Username

* Must contain at least 5 characters
* Must be unique within the database

### Password

* Must contain at least 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one digit
* At least one special character

## Application Workflow

1. Create an account using the Signup page.
2. Log in using valid credentials.
3. Access the Welcome page after successful authentication.
4. Update account information when required.
5. Delete the account with confirmation if needed.

## Learning Outcomes

Through this project, I gained practical experience in:

* Implementing CRUD operations using MySQL
* Integrating Python applications with relational databases
* Building interactive web applications using Streamlit
* Designing secure user authentication workflows
* Performing input validation and exception handling
* Writing modular and reusable Python code
* Executing SQL queries for data management

## Author

**Bhavyashree Poojary**

# Daily Diet Flask API

## Overview

This Flask API provides functionality for managing users and meals. It includes user registration, login, logout, and management of meal records. Authentication is managed using Flask-Login, and passwords are encrypted with bcrypt. Meals are associated with users and can be created, updated, read, or deleted.

## Features

### User Management

- **User Registration**: Create a new user with a username and password. Passwords are securely hashed before storage.
- **User Login**: Authenticate users with their username and password. A successful login establishes a session.
- **User Logout**: End the session of the currently logged-in user.
- **View User Profile**: Retrieve information about a user by their ID, including username.
- **Update User Profile**: Modify user details, including updating passwords (only the user themselves can update their own password).
- **Delete User**: Remove a user from the system. Only administrators can delete users, and users cannot delete their own accounts.

### Meal Management

- **Create Meal**: Add a new meal record associated with the currently logged-in user.
- **Update Meal**: Modify an existing meal record. Only the owner of the meal can update it.
- **Delete Meal**: Remove a meal record. Only the owner of the meal can delete it.
- **View Meal**: Retrieve information about a specific meal record.
- **List Meals**: Retrieve a list of all meal records associated with the currently logged-in user.

## Requirements

- Python 3.x
- Flask
- Flask-Login
- Flask-SQLAlchemy
- bcrypt

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>

2. **Navigate to the project directory:**:
   ```bash
   cd daily-diet-flask-api

3. **Clone the repository**:
   ```bash
   pip install -r requirements.txt

4. **Clone the repository**:
   ```bash
   docker-compose up -d

## Usage

To run the application, execute the following command in your terminal:

  ```bash
  python app.py
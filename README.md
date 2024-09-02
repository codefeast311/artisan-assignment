# FastAPI Chat Application

A modern, efficient, and modular chat application built using FastAPI and MongoDB. This application provides a RESTful API for managing chat messages, allowing users to create, retrieve, update, and delete messages.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project demonstrates a clean and modular approach to building a FastAPI application with MongoDB. It includes the following features:
- Create new messages
- Retrieve all messages
- Update existing messages
- Delete messages

The application follows industry best practices for project structure and code organization, making it easy to maintain and extend.

## Features

- **CRUD Operations**: Create, read, update, and delete chat messages.
- **Modular Design**: Separated concerns into different files and directories.
- **Asynchronous Programming**: Utilizes asynchronous I/O for efficient database operations.
- **Environment Configuration**: Uses environment variables for configuration.

## Technologies

- **FastAPI**: High-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Motor**: Asynchronous MongoDB driver for Python.
- **MongoDB**: NoSQL database for storing messages.
- **Python-dotenv**: For loading environment variables from a `.env` file.

## Setup and Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/fastapi-chat-application.git
   cd fastapi-chat-application
   ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment::

    ```bash
    # On Windows
    venv\Scripts\activate

    # On macOS and Linux
    source venv/bin/activate
    ```

4. Install the required dependencies:
    ```
    Install the required dependencies:
    ```

5. Set up environment variables:

    Create a .env file in the root directory and add your MongoDB URI:

    ```
    MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>/<dbname>?retryWrites=true&w=majority
    ```

## Running the Application

To run the FastAPI application locally, use Uvicorn:

    uvicorn app.main:app --reload

The application will be available at http://127.0.0.1:8000. The interactive API documentation can be accessed at http://127.0.0.1:8000/docs.
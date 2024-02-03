# ProjectMon - Employee and Project Management

ProjectMon is a system for managing information about employees, organizations, projects, and documents. It is implemented using Django and Django REST Framework for the backend, and React for the frontend.

## Key Features

- Registration and storage of data about employees, organizations, projects, and documents.
- Management of information about legal entities and their details.
- Creation and tracking of projects with corresponding documents.
- Storage and management of various types of documents (PDF, Excel, Word, etc.).
- Integration with financial data of organizations and banking details.

## Technologies

- **Django**: Web framework for backend development.
- **Django REST Framework**: Toolkit for creating RESTful APIs.
- **React**: Frontend framework.
- **SQLite**: Database management system.
- **HTML, CSS, JavaScript**: Frontend technologies.

## Installation and Run

### Backend (Django + DRF)

1. Clone the repository:

    ```bash
    git clone https://github.com/rinatovich/ProjectMon.git
    cd ProjectMon/backend
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the server:

    ```bash
    python manage.py runserver
    ```

Django project will be available at http://127.0.0.1:8000/

### Frontend (React)

1. Navigate to the frontend directory:

    ```bash
    cd ../front
    ```

2. Install dependencies:

    ```bash
    npm install
    ```

3. Run the application:

    ```bash
    npm start
    ```

React project will be available at http://localhost:3000/

## Project Structure
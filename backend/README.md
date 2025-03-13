# Event Planner API

This project is a FastAPI application designed to manage events, guests, tasks, and user authentication for the InApp 25th Anniversary celebration.

## Project Structure

```
event-planner
├── backend
│   ├── app
│   │   ├── api
│   │   │   ├── endpoints
│   │   │   │   ├── events.py        # API endpoints for managing events
│   │   │   │   ├── guests.py        # API endpoints for managing guests
│   │   │   │   ├── login.py         # API endpoint for user login
│   │   │   │   ├── tasks.py         # API endpoints for managing tasks
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── core
│   │   │   ├── config.py            # Configuration settings
│   │   │   └── __init__.py
│   │   ├── db
│   │   │   ├── init_db.py           # Database initialization logic
│   │   │   ├── session.py            # Database session management
│   │   │   └── __init__.py
│   │   ├── models
│   │   │   ├── event.py             # Event model definition
│   │   │   ├── guest.py             # Guest model definition
│   │   │   ├── task.py              # Task model definition
│   │   │   ├── user.py              # User model definition
│   │   │   └── __init__.py
│   │   ├── schemas
│   │   │   ├── event.py             # Pydantic schema for events
│   │   │   ├── guest.py             # Pydantic schema for guests
│   │   │   ├── task.py              # Pydantic schema for tasks
│   │   │   ├── user.py              # Pydantic schema for users
│   │   │   └── __init__.py
│   │   ├── main.py                  # Entry point of the application
│   │   └── __init__.py
│   ├── tests
│   │   ├── test_events.py           # Unit tests for events
│   │   ├── test_guests.py           # Unit tests for guests
│   │   ├── test_login.py            # Unit tests for login
│   │   ├── test_tasks.py            # Unit tests for tasks
│   │   └── __init__.py
│   ├── .env                         # Environment variables
│   ├── requirements.txt             # Project dependencies
│   └── README.md                    # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd event-planner/backend
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the `backend` directory and add your database credentials and other necessary environment variables.

5. **Initialize the database:**
   Run the `init_db.py` script to create the database and insert initial data.

6. **Run the application:**
   ```
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

## Usage

- Access the API at `http://localhost:8000/api/`.
- Use the provided endpoints to manage events, guests, tasks, and user authentication.

## Testing

- Run the tests using:
  ```
  pytest
  ```

## License

This project is licensed under the MIT License.
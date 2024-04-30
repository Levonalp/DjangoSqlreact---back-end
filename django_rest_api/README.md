# DjangoSqlreact - Backend

## Project Overview

This backend application is built using Django, providing API services for a React frontend. It demonstrates a robust implementation of RESTful principles and integrates with a PostgreSQL database for data management.

## Key Features

- REST API endpoints for efficient data handling.
- Integration with PostgreSQL for reliable data storage.
- Secure configuration management using environment variables.

## Installation

- Clone the repository: `git clone https://github.com/Levonalp/DjangoSqlreact---back-end.git`
- Install dependencies: `pip install -r requirements.txt`
- Set up PostgreSQL database with the credentials provided in `settings.py`.

## Configuration

Create a `.env` file in the project root with the following variables:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Debug mode (`True` or `False`)
- `ALLOWED_HOSTS`: Configure as needed

## Running the Application

- Execute `python manage.py runserver` to start the Django server.
- The API will be available at `http://localhost:8000/`.

## Security

- Uses Django's security best practices.
- Environment variables for sensitive settings.

## Contribution

Contributions are welcome! Please submit pull requests or open issues for any enhancements or bug fixes.

---

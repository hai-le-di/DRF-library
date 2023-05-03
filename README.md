# DRF Library

This is a simple Library Management System built with Django and Django Rest Framework.

### Getting Started

To get a copy of this project up and running on your local machine, follow these steps:

1. Clone this repository to your local machine using https://github.com/hai-le-di/DRF-library.git
2. Navigate to the project's root directory:
```
cd DRF-library
```
3. Create a virtual environment:
```
python -m venv env
```
4. Activate the virtual environment:
```
source env/bin/activate
```
5. Install the project's dependencies:
```
pip install -r requirements.txt
```
6. Create a .env file in the project's root directory and set the environment variables listed in the .env.sample
7. Run the database migrations:
```
python manage.py migrate
```
8. Create a superuser account:
```
python manage.py createsuperuser
```
9. Start the development server:
```
python manage.py runserver
```
10. Open your web browser and navigate to http://localhost:8000/admin to access the Django admin site. Log in with your superuser account credentials.

## API Endpoints

The API endpoints provided by this project are:

| URL                            | Method | Description                           |
| ------------------------------| ------ | ------------------------------------- |
| /api/books/                    | GET    | Retrieve a list of all books.         |
| /api/books/                    | POST   | Create a new book.                    |
| /api/books/{id}/               | GET    | Retrieve a single book.               |
| /api/books/{id}/               | PUT    | Update a single book.                 |
| /api/books/{id}/               | DELETE | Delete a single book.                 |
| /api/borrowings/               | GET    | Retrieve a list of all borrowings.    |
| /api/borrowings/               | POST   | Create a new borrowing.               |
| /api/borrowings/{id}/          | GET    | Retrieve a single borrowing.          |
| /api/borrowings/{id}/          | PUT    | Update a single borrowing.            |
| /api/borrowings/{id}/          | DELETE | Delete a single borrowing.            |
| /api/borrowings/{id}/return_borrowing/ | POST | Return a borrowing.            |

### Running the Tests

To run the automated tests for this project, navigate to the project's root directory and run the following command:
```
python manage.py test
```

### Built With
* Django - A high-level Python web framework
* Django Rest Framework - A powerful and flexible toolkit for building Web APIs
* Celery - A distributed task queue
* Redis - An in-memory data structure store
* PostgreSQL - A powerful, open source object-relational database system
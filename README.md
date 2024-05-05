## FastAPI SQLAlchemy CRUD Application for Managing Books

This is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI and SQLAlchemy.

## Instructions for Running Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/fastapi-sqlalchemy-crud.git
```

2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Open the `main.py` file and update the `DATABASE_URL` variable with your MySQL database connection URL. Replace `"mysql://username:password@localhost/db_name"` with your database credentials.

4. Run the application locally using Uvicorn:

```bash
uvicorn main:app --reload
```

5. Once the server is running, you can access the Swagger documentation for the API by navigating to the following URL in your web browser:

```
http://127.0.0.1:8000/docs
```

The Swagger UI provides an interactive interface where you can explore and test the different endpoints of the API.

## Available Endpoints

- `GET /books`: Retrieve a list of all books.
- `GET /books/{id}`: Retrieve information about a specific book.
- `POST /books`: Add a new book to the collection.
- `PUT /books/{id}`: Update information about a specific book.
- `DELETE /books/{id}`: Delete a book from the collection.

## Input Validation

- Ensure that required fields are provided when creating a book (title, author, year, isbn).
- Validate input types and formats (e.g., year should be an integer, isbn should be a string).

Feel free to explore and interact with the API using the provided Swagger documentation.
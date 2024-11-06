# FastAPI Blog Authentication Simple Token

This project is a simple blog application built with **FastAPI**, demonstrating basic **authentication** using a simple token-based system. It shows how to implement user registration, login, and token-based authentication with FastAPI.

## Features

- **User Authentication**: Users can register, log in, and authenticate using simple token-based authentication (JWT).
- **Blog CRUD**: Basic CRUD functionality for creating, reading, updating, and deleting blog posts.
- **FastAPI**: High-performance web framework used to build the API.
- **Security**: Implements basic security measures using JWT for token-based authentication.

## Requirements

- **Python 3.x**
- **FastAPI**: The web framework used for building the API.
- **Pydantic**: For data validation.
- **PyJWT**: To handle JWT token encoding and decoding.
- **Uvicorn**: ASGI server to run the FastAPI app.

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/shahramsamar/FastApi_Blog_Authentication_Simple_Token.git
    cd FastApi_Blog_Authentication_Simple_Token
    ```

2. **Install Dependencies:**

    You can install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the API:**

    To start the FastAPI server, use the following command:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the API at `http://127.0.0.1:8000`.

4. **Access the API Documentation:**

    FastAPI automatically generates Swagger UI documentation for your API at `http://127.0.0.1:8000/docs`.

### Project Structure

- `main.py`: Contains the FastAPI app, routes, and JWT authentication logic.
- `models.py`: Contains Pydantic models for data validation.
- `security.py`: Contains logic for encoding and decoding JWT tokens.
- `requirements.txt`: Lists the required Python packages.

### Example Usage

- **User Registration**: Send a POST request to `/register/` with user details.

    Example:

    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/register/' \
      -H 'Content-Type: application/json' \
      -d '{
      "username": "newuser",
      "password": "password123"
    }'
    ```

- **User Login**: Send a POST request to `/login/` with username and password to receive a JWT token.

    Example:

    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/login/' \
      -H 'Content-Type: application/json' \
      -d '{
      "username": "newuser",
      "password": "password123"
    }'
    ```

- **Create Blog Post**: Send a POST request to `/blog/` with the required blog data (authentication required).

    Example:

    ```bash
    curl -X 'POST' \
      'http://127.0.0.1:8000/blog/' \
      -H 'Authorization: Bearer <your_token>' \
      -d '{
      "title": "My First Blog Post",
      "content": "This is the content of my first blog post."
    }'
    ```

- **Get Blog Posts**: Send a GET request to `/blog/` to retrieve all blog posts.

    Example:

    ```bash
    curl 'http://127.0.0.1:8000/blog/'
    ```

- **Delete Blog Post**: Send a DELETE request to `/blog/{post_id}/` to delete a specific blog post.

    Example:

    ```bash
    curl -X 'DELETE' \
      'http://127.0.0.1:8000/blog/1/' \
      -H 'Authorization: Bearer <your_token>'
    ```

## Contributing

Feel free to fork the repository and submit pull requests for new features, improvements, or bug fixes.

## License

This project is open-source and available for educational purposes.

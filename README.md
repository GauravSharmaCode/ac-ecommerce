# product_listing_app

A Django backend for an e-commerce platform, featuring user registration, JWT authentication, and modular apps for accounts, products, portfolio, contact, and orders. Built with Django REST Framework and ready for secure API development.

## Features

- User registration and JWT-based authentication
- Modular Django apps: accounts, products, portfolio, contact, orders
- RESTful API endpoints for easy integration with frontend or mobile apps
- Built-in Django admin for data management

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (recommended)

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/yourusername/product_listing_app.git
   cd product_listing_app
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

5. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Registration

- **POST** `/api/accounts/register/`
  - Request body:
    ```json
    {
      "username": "yourusername",
      "email": "youremail@example.com",
      "password": "yourpassword"
    }
    ```

### Login (JWT Token)

- **POST** `/api/token/`
  - Request body:
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    ```
  - Response:
    ```json
    {
      "refresh": "your-refresh-token",
      "access": "your-access-token"
    }
    ```

## Project Structure

```
accounts/      # User registration and authentication
products/      # Product management
portfolio/     # Portfolio or showcase
contact/       # Contact form or messages
orders/        # Order management
backend/       # Django project settings and URLs
```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)

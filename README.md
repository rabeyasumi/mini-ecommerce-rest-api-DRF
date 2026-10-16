# Mini E-commerce REST API

A Mini E-commerce REST API built with Django and Django REST Framework (DRF). This project demonstrates CRUD operations, token authentication, product filtering, searching, ordering, pagination, and order management.

## Technologies Used

- Python
- Django
- Django REST Framework
- django-filter
- SQLite
- Postman

## Features

### Category API
- Create, list, retrieve, update, and delete categories.

### Product API
- Create, list, retrieve, update, and delete products.
- Search products by name.
- Filter by category and price range.
- Order products by price or creation date.
- Paginate product results.

### Authentication
- Token-based authentication.
- Read-only access to categories and products without authentication.
- Authentication required for write operations.
- Authenticated users can create and view their own orders.

### Order API
- Create orders for products.
- Automatically calculate the total price.
- Validate requested quantity against available stock.
- Reduce product stock after successful order creation.
- Restrict order access to the owner.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   cd YOUR_PROJECT_FOLDER
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET, POST | `/api/categories/` | List and create categories |
| GET, PUT, PATCH, DELETE | `/api/categories/<id>/` | Retrieve, update, delete category |
| GET, POST | `/api/products/` | List and create products |
| GET, PUT, PATCH, DELETE | `/api/products/<id>/` | Retrieve, update, delete product |
| POST | `/api/token/` | Obtain authentication token |
| GET, POST | `/api/orders/` | List own orders and create an order |
| GET | `/api/orders/<id>/` | Retrieve own order |

## Product Filtering Examples

- Search: `/api/products/?search=phone`
- Category: `/api/products/?category=1`
- Minimum price: `/api/products/?min_price=1000`
- Maximum price: `/api/products/?max_price=5000`
- Price range: `/api/products/?min_price=1000&max_price=5000`
- Ascending price: `/api/products/?ordering=price`
- Descending price: `/api/products/?ordering=-price`
- Pagination: `/api/products/?page=2`

## Authentication

Send a POST request to `/api/token/` with a valid username and password to obtain a token.

For protected requests, include this HTTP header:

```text
Authorization: Token YOUR_TOKEN
```

## Testing

API endpoints can be tested using Postman.

## License

This project was created for educational purposes.
# DRF-Project-1
## Project Structure

**Core Django Files:**

- `manage.py` - Django management script
- `books_project/` - Main project directory with settings and URLs
- `books/` - Books app with models, views, serializers, and URLs


**Key Features:**

### 1. Book Model

- **ID**: UUID4 primary key
- **Name**: Book title (CharField)
- **Category**: Predefined choices (fiction, non-fiction, etc.)
- **Created By**: Foreign key to User model
- **Timestamps**: Created at and updated at fields


### 2. API Endpoints

- `GET/POST /api/books/` - List all books or create new book
- `GET/PUT/DELETE /api/books/<uuid>/` - Retrieve, update, or delete specific book
- `GET /api/books/categories/` - Get available book categories
- `GET /api/books/my-books/` - Get current user's books


### 3. Authentication & Permissions

- Uses Django's built-in authentication
- Users can only update/delete their own books
- All endpoints require authentication


### 4. Additional Features

- **Filtering**: Filter books by category using query parameters
- **Pagination**: Built-in pagination (20 items per page)
- **CORS**: Configured for frontend integration
- **Admin Interface**: Django admin integration for easy management

## Setup Instructions

1. **Install Dependencies:**
```
pip install -r requirements.txt
```
2. **Run Setup Script:**
```
python scripts/setup_project.py
```
3. **Start Development Server:**
```
python manage.py runserver
```

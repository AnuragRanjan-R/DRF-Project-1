#!/usr/bin/env python
"""
Test script to demonstrate API functionality
"""
import requests
import json

# Base URL for the API
BASE_URL = 'http://127.0.0.1:8000/api'

def test_api():
    """Test the Books API endpoints"""
    
    print("Testing Books API...")
    print("Make sure the Django server is running: python manage.py runserver")
    print("And you have created a superuser account\n")
    
    # You'll need to authenticate first
    # For testing, you can use Django admin session or implement token authentication
    
    session = requests.Session()
    
    # Test endpoints (you'll need to be authenticated)
    endpoints = [
        ('GET', f'{BASE_URL}/books/', 'List all books'),
        ('GET', f'{BASE_URL}/books/categories/', 'Get book categories'),
        ('GET', f'{BASE_URL}/books/my-books/', 'Get my books'),
    ]
    
    print("Available API endpoints:")
    for method, url, description in endpoints:
        print(f"{method} {url} - {description}")
    
    print("\nSample book creation data:")
    sample_book = {
        "name": "The Great Gatsby",
        "category": "fiction"
    }
    print(json.dumps(sample_book, indent=2))
    
    print("\nTo test the API:")
    print("1. Start the server: python manage.py runserver")
    print("2. Login to Django admin: http://127.0.0.1:8000/admin/")
    print("3. Use tools like Postman or curl to test the endpoints")
    print("4. Include authentication headers in your requests")

if __name__ == '__main__':
    test_api()

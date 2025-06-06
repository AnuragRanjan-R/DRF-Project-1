#!/usr/bin/env python
"""
Setup script to initialize the Django project
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

def setup_django_project():
    """Initialize Django project with migrations and superuser"""
    
    print("Setting up Django project...")
    
    # Add project root to Python path
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, project_root)
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')
    
    # Setup Django
    django.setup()
    
    print("1. Making migrations...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    
    print("2. Running migrations...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("3. Creating superuser...")
    print("Please create a superuser account:")
    execute_from_command_line(['manage.py', 'createsuperuser'])
    
    print("\nSetup complete!")
    print("You can now run the server with: python manage.py runserver")
    print("API endpoints will be available at:")
    print("- GET/POST /api/books/ - List/Create books")
    print("- GET/PUT/DELETE /api/books/<uuid>/ - Retrieve/Update/Delete specific book")
    print("- GET /api/books/categories/ - Get available categories")
    print("- GET /api/books/my-books/ - Get current user's books")

if __name__ == '__main__':
    setup_django_project()

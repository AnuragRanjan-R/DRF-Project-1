from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateView.as_view(), name='book-list-create'),
    path('books/<uuid:id>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/categories/', views.book_categories, name='book-categories'),
    path('books/my-books/', views.my_books, name='my-books'),
]

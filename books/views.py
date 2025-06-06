from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer, BookCreateUpdateSerializer


class BookListCreateView(generics.ListCreateAPIView):
    """
    List all books or create a new book.
    """
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Book.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookCreateUpdateSerializer
        return BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return BookCreateUpdateSerializer
        return BookSerializer
    
    def perform_update(self, serializer):
        # Ensure only the owner can update their books
        book = self.get_object()
        if book.created_by != self.request.user:
            return Response(
                {'error': 'You can only update your own books.'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        serializer.save()
    
    def perform_destroy(self, instance):
        # Ensure only the owner can delete their books
        if instance.created_by != self.request.user:
            return Response(
                {'error': 'You can only delete your own books.'}, 
                status=status.HTTP_403_FORBIDDEN
            )
        instance.delete()


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def book_categories(request):
    """
    Get all available book categories.
    """
    categories = [{'value': choice[0], 'label': choice[1]} for choice in Book.CATEGORY_CHOICES]
    return Response(categories)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def my_books(request):
    """
    Get books created by the current user.
    """
    books = Book.objects.filter(created_by=request.user)
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

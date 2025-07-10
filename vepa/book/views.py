from .models import Book
from .serializer import BookSerializer
from rest_framework import viewsets, mixins



class BookView(viewsets.ModelViewSet, mixins.ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

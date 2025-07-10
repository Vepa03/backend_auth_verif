from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id' , 'title', 'description' , 'image', 'category', 'book', 'author']

class BookForCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = ['id' , 'title', 'description' , 'image', 'category', 'book', 'author']
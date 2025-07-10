from django.db import models
from category.models import Category

class Book(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField(upload_to='uploads')
    author = models.CharField()
    book = models.FileField(upload_to='uploads', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title

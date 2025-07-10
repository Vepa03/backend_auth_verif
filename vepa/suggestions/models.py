from django.db import models

class Suggestion(models.Model):
    name = models.CharField()
    book = models.FileField(upload_to='uploads' )
    description = models.TextField()

    def __str__(self):
        return self.name
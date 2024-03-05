from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    published_year = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book_name', 'author')
from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    book_author = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/')
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    rating = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} reviewed {self.book.title}"
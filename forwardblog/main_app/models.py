from django.db import models
from django.forms import DateTimeInput
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(null=True, blank=True)
    date_edited= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'post_id': self.id})


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(null=True, blank=True)
    date_edited= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'book_id': self.id})
   
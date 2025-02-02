from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(null=True, blank=True)
    date_edited= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



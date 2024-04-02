# main/models.py
from django.db import models

class Blog(models.Model):
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', default='images/best2.jpg')
    time_published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    brief = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

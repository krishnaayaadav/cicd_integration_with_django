from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug   = models.SlugField(max_length=255)

    def __str__(self):
        return f'Title: {self.title} | Author: {self.author}'
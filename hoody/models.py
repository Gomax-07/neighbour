from django.db import models

from django.urls import reverse


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    occupantsCount = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70)


class Business(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

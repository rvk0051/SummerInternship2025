from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# defining 'Post' model which creates a table with the following 5 attributes.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# 'defining 'Profile' model which extends 'User' model, without changing 'User' class.
# 'Profile' class have all the attributes which 'User' have and the 'author_name'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name




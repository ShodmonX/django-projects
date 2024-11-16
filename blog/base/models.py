from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date
from django_ckeditor_5.fields import CKEditor5Field

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile-images/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    telegram_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    website_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    body = CKEditor5Field('Body')
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s - %s" % (self.post.title, self.author.username, self.body[:15])
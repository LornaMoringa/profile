from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image_caption = models.TextField()

class Profile(models.Model):
  picture = CloudinaryField('image')
  bio = models.TextField()
  user = models.OneToOneField(User,on_delete = models.CASCADE)

class Comment(models.Model):
  comment = models.TextField()
  post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='comments')
  user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')
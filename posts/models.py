from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Post(models.Model):
    image = ClaudinaryField('image')
    name = CharField(max_length=30)
    user = model

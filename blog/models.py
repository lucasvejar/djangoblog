from django.db import models
from django.utils import  timezone


class Post(models.Model):
    # atributes
    description = models.CharField(max_length = 200)
    img_path = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default=timezone.now)

    # methods
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description


class User(models.Model):
    # atributes
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

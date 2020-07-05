from django.db import models
from django.utils import  timezone



class User(models.Model):
    user = models.CharField(max_length = 30)
    user_name = models.CharField(max_length = 40)
    biography = models.CharField(max_length = 200)
    profile_pic = models.CharField(max_length = 200)

    def __str__(self):
        return self.user_name


class Post(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    img_path = models.CharField(max_length = 200)
    created_date = models.DateTimeField(default=timezone.now)

    # methods
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    users_who_commented = models.ForeignKey('User',on_delete=models.CASCADE)
    content = models.TextField()
    liked = models.IntegerField()

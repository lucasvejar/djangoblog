from django.contrib import admin
from .models import Post, User, Comment, Story

# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Story)
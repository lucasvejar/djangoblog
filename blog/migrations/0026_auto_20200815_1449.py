# Generated by Django 3.0.7 on 2020-08-15 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0025_friends_date_begin'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='users',
            field=models.ManyToManyField(to='blog.CustomUser'),
        ),
        migrations.RemoveField(
            model_name='friends',
            name='user',
        ),
        migrations.AddField(
            model_name='friends',
            name='user',
            field=models.OneToOneField(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
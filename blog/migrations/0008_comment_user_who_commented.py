# Generated by Django 3.0.7 on 2020-07-05 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_who_commented',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200705_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]

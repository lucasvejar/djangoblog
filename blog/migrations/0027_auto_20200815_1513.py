# Generated by Django 3.0.7 on 2020-08-15 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20200815_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='friend',
            new_name='friends',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]

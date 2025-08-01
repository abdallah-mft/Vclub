# Generated by Django 5.2.4 on 2025-08-01 17:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_customuser_ppf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='ppf',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video'),
        ),
    ]

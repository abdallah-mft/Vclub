# Generated by Django 5.2.4 on 2025-08-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_bio_customuser_field_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ppf',
            field=models.ImageField(blank=True, null=True, upload_to='ppf/'),
        ),
    ]

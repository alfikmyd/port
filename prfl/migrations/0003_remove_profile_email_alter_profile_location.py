# Generated by Django 4.2.19 on 2025-02-15 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prfl', '0002_rename_profile_picture_profile_profile_pics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

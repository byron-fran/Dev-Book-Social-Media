# Generated by Django 5.0.6 on 2024-06-05 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo_profile',
            field=models.ImageField(blank=True, null=True, upload_to='profiles_photo/'),
        ),
    ]
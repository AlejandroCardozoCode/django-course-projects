# Generated by Django 5.0.3 on 2024-03-28 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_moviedata_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/movies_images/default.jpg', upload_to='images/movies_images/'),
        ),
    ]

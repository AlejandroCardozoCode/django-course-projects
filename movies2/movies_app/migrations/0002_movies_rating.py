# Generated by Django 5.0.3 on 2024-03-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='rating',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1a1 on 2020-06-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='library/static/images/default.jpg', upload_to='library/static/images'),
        ),
    ]
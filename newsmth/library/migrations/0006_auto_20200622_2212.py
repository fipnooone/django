# Generated by Django 3.1a1 on 2020-06-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200622_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images'),
        ),
    ]

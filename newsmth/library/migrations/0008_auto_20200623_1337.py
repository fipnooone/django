# Generated by Django 3.1a1 on 2020-06-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_auto_20200623_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='images/default.gif', upload_to='images'),
        ),
    ]
# Generated by Django 3.1a1 on 2020-06-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20200623_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]

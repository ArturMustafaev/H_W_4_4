# Generated by Django 4.0.5 on 2022-06-27 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='movies'),
        ),
    ]

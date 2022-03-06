# Generated by Django 3.2.11 on 2022-02-08 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelis', '0004_auto_20220202_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='link',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-21 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_tour_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='image',
            field=models.ImageField(upload_to='media/img/destinations'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='media/img/tours'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(upload_to='media/img/tours'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='status',
            field=models.BooleanField(default=False, verbose_name='publish it now'),
        ),
        migrations.AlterField(
            model_name='tourdetail',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
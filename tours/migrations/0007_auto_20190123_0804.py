# Generated by Django 2.1.5 on 2019-01-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_book_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

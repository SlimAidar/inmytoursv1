# Generated by Django 2.1.5 on 2019-01-23 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='message',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
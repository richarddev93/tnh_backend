# Generated by Django 3.0.2 on 2020-08-07 00:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0016_auto_20200712_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='img',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]

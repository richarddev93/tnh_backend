# Generated by Django 3.0.2 on 2020-03-07 15:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicos', '0003_auto_20200307_1225'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Imagens',
            new_name='ImagensServ',
        ),
    ]

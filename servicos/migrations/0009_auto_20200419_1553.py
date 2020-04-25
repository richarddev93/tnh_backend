# Generated by Django 3.0.2 on 2020-04-19 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicos', '0008_favoritos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritos',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.Servico'),
        ),
        migrations.AlterField(
            model_name='favoritos',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

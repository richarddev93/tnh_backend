# Generated by Django 3.0.2 on 2020-04-19 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0007_auto_20200308_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('servico', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='correo@example.com', max_length=254, unique=True),
        ),
    ]

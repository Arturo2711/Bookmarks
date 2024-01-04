# Generated by Django 5.0.1 on 2024-01-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_usuario_correo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjetiosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('peso_actual_kilogramos', models.FloatField()),
                ('peso_objetivo_kilogramos', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]

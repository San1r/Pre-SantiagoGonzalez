# Generated by Django 5.1 on 2024-08-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autorizaciones', '0002_rename_practicas_practica'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afiliado',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='afiliado',
            name='telefono',
        ),
        migrations.AddField(
            model_name='afiliado',
            name='dni',
            field=models.CharField(default='Sin Dni', max_length=8, unique=True),
        ),
        migrations.AddField(
            model_name='afiliado',
            name='email',
            field=models.CharField(default='Sin dni', max_length=100),
        ),
    ]

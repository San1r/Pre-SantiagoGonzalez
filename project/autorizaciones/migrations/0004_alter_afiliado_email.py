# Generated by Django 5.1 on 2024-08-28 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autorizaciones', '0003_remove_afiliado_domicilio_remove_afiliado_telefono_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliado',
            name='email',
            field=models.CharField(default='Sin email', max_length=100),
        ),
    ]

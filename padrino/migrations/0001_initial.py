# Generated by Django 4.1.7 on 2023-05-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Padrino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('tipo_persona', models.CharField(max_length=255)),
                ('estrato', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('correo', models.EmailField(max_length=254)),
                ('tiempo_apadrinando', models.TextField()),
                ('campo', models.CharField(max_length=255)),
            ],
        ),
    ]

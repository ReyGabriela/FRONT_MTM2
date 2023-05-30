# Generated by Django 4.1.7 on 2023-05-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('nui', models.IntegerField()),
                ('fecha_inicio_tratamiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
                ('seguro_funebre', models.CharField(max_length=255)),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('direccion_residencia', models.CharField(max_length=255)),
            ],
        ),
    ]

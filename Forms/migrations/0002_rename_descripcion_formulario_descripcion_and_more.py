# Generated by Django 5.1.4 on 2024-12-12 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulario',
            old_name='descripcion',
            new_name='Descripcion',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='fecha_creacion',
            new_name='Fecha_Creacion',
        ),
        migrations.RenameField(
            model_name='formulario',
            old_name='nombre',
            new_name='Nombre',
        ),
    ]

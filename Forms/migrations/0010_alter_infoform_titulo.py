# Generated by Django 5.1.4 on 2024-12-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0009_alter_infoform_opciones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoform',
            name='titulo',
            field=models.CharField(max_length=40),
        ),
    ]
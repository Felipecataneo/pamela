# Generated by Django 3.2.5 on 2021-11-17 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_rename_category_paciente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='title',
            new_name='nome',
        ),
    ]

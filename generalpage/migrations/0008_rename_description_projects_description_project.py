# Generated by Django 4.0 on 2022-01-12 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generalpage', '0007_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='description',
            new_name='description_project',
        ),
    ]

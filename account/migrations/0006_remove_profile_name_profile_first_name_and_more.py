# Generated by Django 4.0 on 2021-12-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_username_alter_profile_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

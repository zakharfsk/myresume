# Generated by Django 3.2.8 on 2021-11-21 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id' , models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('name_company', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('time_jobs', models.CharField(max_length=100)),
            ],
        ),
    ]

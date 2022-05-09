# Generated by Django 3.2.8 on 2021-11-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalpage', '0003_myskills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'ordering': ['id', '-time_jobs'], 'verbose_name': 'Досвід роботи', 'verbose_name_plural': 'Досвід роботи'},
        ),
        migrations.AlterModelOptions(
            name='myskills',
            options={'ordering': ['id', 'title'], 'verbose_name': 'Мої навички', 'verbose_name_plural': 'Мої навички'},
        ),
        migrations.AlterModelOptions(
            name='mysoftskills',
            options={'ordering': ['id', 'name_skill'], 'verbose_name': 'Soft Skills', 'verbose_name_plural': 'Soft Skills'},
        ),
        migrations.AlterField(
            model_name='jobs',
            name='content',
            field=models.TextField(blank=True, verbose_name='Опис роботи'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='name_company',
            field=models.CharField(max_length=100, verbose_name='Компанія'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='time_jobs',
            field=models.CharField(max_length=100, verbose_name='Термін роботи'),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Тип роботи'),
        ),
    ]

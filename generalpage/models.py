from django.db import models


class Jobs(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Тип роботи')
    name_company = models.CharField(max_length=100, verbose_name = 'Компанія')
    content = models.TextField(blank = True, verbose_name = 'Опис роботи')
    time_jobs = models.CharField(max_length = 100, verbose_name = 'Термін роботи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Досвід роботи'
        verbose_name_plural = 'Досвід роботи'
        ordering = ['id', '-time_jobs']

class MySkills(models.Model):
    title = models.CharField(max_length = 100, blank = True)
    description = models.TextField(blank = True)
    count = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мої навички'
        verbose_name_plural = 'Мої навички'
        ordering = ['id', 'title']
        
class Projects(models.Model):
    name_project = models.CharField(
        max_length = 100, blank = True, verbose_name = 'Назва проекта')
    description_project = models.TextField(
        blank = True, verbose_name = 'Опис проекта')
    link_on_github = models.CharField(
        max_length = 100, blank = True, verbose_name = 'Силка на GitHub проекта')

    def __str__(self):
        return self.name_project

    class Meta:
        verbose_name = 'Мої проекти'
        verbose_name_plural = 'Мої проекти'
        ordering = ['id', 'name_project']
from django.contrib import admin
from .models import *


class JobsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name_company', 'time_jobs')
    list_display_links = ('title',)
    search_fields = ('title', 'time_jobs')
    list_filter = ('time_jobs',)


class MySkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)
    sortable = ('id',)

class MyProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_project', 'description_project')
    list_display_links = ('name_project',)
    search_fields = ('name_project',)
    sortable = ('id',)

admin.site.register(Jobs, JobsAdmin)
admin.site.register(MySkills, MySkillsAdmin)
admin.site.register(Projects, MyProjectsAdmin)
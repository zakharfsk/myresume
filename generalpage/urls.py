from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.urls import path

from .views import *

urlpatterns = [
    path('', general, name = 'home'),
    path('jobs/', expirienceJobs, name = 'expirience_jobs'),
    path('jobs/<int:job_id>', select_jobs, name = 'select_job'),
    path('skills/', mySkills, name = 'skills'),
    path('projects/', myProjects, name = 'my_projects'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
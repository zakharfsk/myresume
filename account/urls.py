from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path(r'<str:username>', profile, name = 'users-profile'),
    path(r'login/', page_login, name = 'login'),
    path(r'logout/', logoutUser, name = 'logout'),
    path(r'register/', page_register, name = 'register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
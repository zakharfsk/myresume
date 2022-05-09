from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('<str:username>', profile, name = 'users-profile'),
    path('login/', page_login, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('register/', page_register, name = 'register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
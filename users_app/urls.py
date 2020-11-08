from django.urls import path, include
from .views import index, users


urlpatterns = [
    path('', index, name = 'index_url'), 
    path('users/', users, name = 'users_url',)  
]
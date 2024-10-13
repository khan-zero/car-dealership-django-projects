from django.urls import path, include
from .views import index, info, login_view, logout_view, register_view, dashboard

urlpatterns = [
    path('', index, name = 'index'),
    path('info/', info, name = 'info'),
    
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    
    path('dashboard/', dashboard, name = 'dash'),
]

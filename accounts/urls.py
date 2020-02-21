from django.urls import path, include
from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views
from main_app.views import profile

urlpatterns = [
    path('', TemplateView.as_view(template_name='social_app/index.html')),
    url(r'^', include('allauth.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', profile, name='profile'),
]

# timer_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('success/<str:user_code>/', views.success, name='success'),
    path('policy/', views.policy, name='policy'),  # Добавьте маршрут для политики
    path('instagram-story/<str:user_code>/', views.generate_instagram_story_image, name='instagram_story'),
]

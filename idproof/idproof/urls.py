# idproof/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),  # Подключаем маршруты для капчи
    path('', include('timer_app.urls')),  # Подключаем маршруты вашего приложения
]

# timer_app/models.py

from django.db import models
import shortuuid

def generate_short_uuid():
    return shortuuid.uuid()[:8]  # Генерирует уникальный код длиной 8 символов

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_code = models.CharField(
        max_length=16,
        unique=True,
        default=generate_short_uuid
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
# idproof/settings.py

import os
from pathlib import Path

# Основные настройки проекта
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-<your_secret_key_here>'
DEBUG = True  # Установите False в продакшене

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.1.76']  # Добавьте домены для продакшена

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'timer_app',  # Ваше приложение
    'captcha',    # Приложение для работы с капчей
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'idproof.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Путь к глобальным шаблонам
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'idproof.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Локализация
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Путь к статическим файлам

# Настройки SMTP для отправки писем
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # SMTP-сервер Gmail
EMAIL_PORT = 587  # Порт для TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'semeniskan@gmail.com'  # Ваш email
EMAIL_HOST_PASSWORD = 'ebvf izib aqqz jrov'  # Пароль приложения
DEFAULT_FROM_EMAIL = 'semeniskan@gmail.com'  # Отправитель

# По умолчанию Django использует SQLite
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки для django-simple-captcha
CAPTCHA_IMAGE_SIZE = (200, 50)  # Размер изображения капчи (как поле ввода)
CAPTCHA_FONT_SIZE = 22  # Размер шрифта
CAPTCHA_LENGTH = 4  # Количество символов в капче
CAPTCHA_BACKGROUND_COLOR = '#1E3A8A'  # Цвет фона
CAPTCHA_FOREGROUND_COLOR = '#FFD95A'  # Цвет текста

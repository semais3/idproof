# ID Proof - Django Web Application

Веб-приложение для проверки подлинности документов с использованием Django.

## Особенности

- 🔐 Система проверки с капчей
- 📧 Отправка email уведомлений
- 📱 Адаптивный дизайн
- 🚀 Готов к развертыванию на Render.com
- 🔒 Безопасные настройки для продакшена

## Технологии

- **Backend**: Django 5.2.3
- **Database**: SQLite (разработка) / PostgreSQL (продакшен)
- **Frontend**: HTML, CSS, JavaScript
- **Captcha**: django-simple-captcha
- **Deployment**: Render.com с Gunicorn

## Установка и запуск

### Локальная разработка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd idproof
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
python manage.py migrate
```

5. Запустите сервер разработки:
```bash
python manage.py runserver
```

Приложение будет доступно по адресу `http://127.0.0.1:8000/`

### Запуск на локальной сети

```bash
python manage.py runserver 192.168.1.76:8000
```

## Развертывание на Render.com

1. Создайте аккаунт на [Render.com](https://render.com)
2. Подключите ваш GitHub репозиторий
3. Render автоматически обнаружит `render.yaml` и развернет приложение
4. Настройте переменные окружения:
   - `SECRET_KEY` (автоматически генерируется)
   - `EMAIL_HOST_PASSWORD` (пароль приложения Gmail)

## Структура проекта

```
idproof/
├── idproof/
│   ├── settings.py           # Основные настройки
│   ├── settings_production.py # Настройки для продакшена
│   ├── urls.py
│   └── wsgi.py
├── timer_app/               # Основное приложение
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── ...
├── static/                  # Статические файлы
├── templates/              # HTML шаблоны
├── requirements.txt        # Python зависимости
├── render.yaml            # Конфигурация Render.com
└── build.sh              # Скрипт сборки
```

## Переменные окружения

### Разработка
- `DEBUG=True`
- `SECRET_KEY` - секретный ключ Django

### Продакшен
- `DEBUG=False`
- `SECRET_KEY` - секретный ключ (генерируется автоматически на Render)
- `DATABASE_URL` - URL базы данных PostgreSQL
- `EMAIL_HOST_PASSWORD` - пароль приложения Gmail

## Безопасность

- ✅ HTTPS принудительно в продакшене
- ✅ HSTS заголовки
- ✅ XSS защита
- ✅ CSRF защита
- ✅ Secure cookies
- ✅ Переменные окружения для секретов

## Лицензия

Этот проект предназначен для личного использования.

## Контакты

Email: semeniskan@gmail.com

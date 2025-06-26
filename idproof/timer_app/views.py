# timer_app/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import User
from PIL import Image, ImageDraw, ImageFont
import io
import os
from django.conf import settings


def home(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Проверяем, существует ли уже пользователь с таким email или username
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Пользователь с этим email уже зарегистрирован.')
            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Пользователь с этим именем уже зарегистрирован.')
            else:
                # Создаем нового пользователя
                user = User.objects.create(username=username, email=email)

                # Отправляем письмо с кодом
                try:
                    send_code_to_email(email, user.user_code)
                    messages.success(request, 'Регистрация прошла успешно! Код отправлен на вашу почту.')
                except Exception as e:
                    messages.error(request, 'Не удалось отправить письмо. Попробуйте позже.')

                # Перенаправляем на страницу успешной регистрации
                return redirect('success', user_code=user.user_code)
    else:
        form = RegistrationForm()

    return render(request, 'timer_app/home.html', {'form': form})


def success(request, user_code):
    try:
        user = User.objects.get(user_code=user_code)
        return render(request, 'timer_app/success.html', {'code': user.user_code})
    except User.DoesNotExist:
        return render(request, 'timer_app/error.html', {'message': 'Пользователь не найден'})


def generate_instagram_story_image(request, user_code):
    try:
        user = User.objects.get(user_code=user_code)
        # Create an image with gradient background
        img = Image.new('RGB', (1080, 1920), color=(30, 58, 138))  # Dark blue background
        d = ImageDraw.Draw(img)
        
        # Use default font
        try:
            # Try to load default system font
            font_large = ImageFont.truetype("arial.ttf", 100)
            font_medium = ImageFont.truetype("arial.ttf", 60)
            font_small = ImageFont.truetype("arial.ttf", 45)
        except:
            # Fallback to default font
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Title (top left)
        d.text((80, 100), "idproof.tech", font=font_medium, fill=(255, 217, 90))

        # User code (center)
        code_text = f"Ваш код: {user.user_code}"
        # Calculate text size to center it
        bbox = d.textbbox((0, 0), code_text, font=font_large)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (1080 - text_width) // 2
        y = (1920 - text_height) // 2
        d.text((x, y), code_text, font=font_large, fill=(255, 255, 255))

        # Description (bottom)
        desc_text = "Хочешь такой же?"
        desc_text2 = "переходи на idproof.tech"
        
        # Calculate position for bottom text
        bbox1 = d.textbbox((0, 0), desc_text, font=font_small)
        bbox2 = d.textbbox((0, 0), desc_text2, font=font_small)
        width1 = bbox1[2] - bbox1[0]
        width2 = bbox2[2] - bbox2[0]
        
        x1 = (1080 - width1) // 2
        x2 = (1080 - width2) // 2
        
        d.text((x1, 1650), desc_text, font=font_small, fill=(255, 217, 90))
        d.text((x2, 1720), desc_text2, font=font_small, fill=(255, 217, 90))

        # Save to a BytesIO object
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG', quality=95)
        img_io.seek(0)

        response = HttpResponse(img_io.read(), content_type='image/jpeg')
        response['Content-Disposition'] = f'attachment; filename="idproof_story_{user_code}.jpg"'
        return response
    except User.DoesNotExist:
        return render(request, 'timer_app/error.html', {'message': 'Пользователь не найден'})

def policy(request):
    return render(request, 'timer_app/policy.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Проверяем, существует ли уже пользователь с таким email или username
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Пользователь с этим email уже зарегистрирован.')
            elif User.objects.filter(username=username).exists():
                form.add_error('username', 'Пользователь с этим именем уже зарегистрирован.')
            else:
                # Создаем нового пользователя
                user = User.objects.create(username=username, email=email)

                # Отправляем письмо с кодом
                try:
                    send_code_to_email(email, user.user_code)
                    messages.success(request, 'Регистрация прошла успешно! Код отправлен на вашу почту.')
                except Exception as e:
                    messages.error(request, 'Не удалось отправить письмо. Попробуйте позже.')

                # Перенаправляем на страницу успешной регистрации
                return redirect('success', user_code=user.user_code)
    else:
        form = RegistrationForm()

    return render(request, 'timer_app/register.html', {'form': form})


def send_code_to_email(user_email, user_code):
    subject = 'Ваш уникальный код IDPROOF'
    html_message = render_to_string('timer_app/email_template.html', {'code': user_code})
    plain_message = strip_tags(html_message)  # Текстовая версия письма
    from_email = 'ваш_email@gmail.com'  # Укажите ваш email
    recipient_list = [user_email]

    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        html_message=html_message,
    )

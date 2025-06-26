from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .widgets import CaptchaBase
from .helpers import (
    get_version,
    proxy_storage,
    setting,
    set_session_store,
    import_from_settings,
)
from .models import CaptchaStore
from .signals import captcha_test_passed, captcha_test_failed

class CaptchaField(forms.Field):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = kwargs.get('widget', ReCaptchaV2Checkbox())
        self.required = True
        self.error_messages.update({
            'invalid': _('Invalid CAPTCHA'),
        })

    def clean(self, value):
        if not value:
            raise ValidationError(self.error_messages['invalid'], code='invalid')
        return value
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


def user_exists(value):
    if not User.objects.filter(username=value).exists():
        raise ValidationError('Такого пользователя не существует!')

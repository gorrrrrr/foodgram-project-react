import re

from django.conf import settings
from django.core.exceptions import ValidationError

USERNAME_REGEX = r'^[\w.@+-]+$'
EMAIL_REGEX = (r'^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@'
               r'[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
PASSWORD_REGEX = (r'^(?=.*?[A-Z])(?=.*?[a-z])'
                  r'(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).$')
PASSWORD_MIN_LENGTH = 8
PASSWORD_REGEXES = (
    (r'.{8,}', 'В пароле должно быть не менее 8 символов.'),
    (r'.*?[A-Z].*?', 'В пароле должна быть хотя бы одна заглавная буква.'),
    (r'.*?\d+.*?', 'В пароле должна быть хотя бы одна цифра.'),
    (r'.*?[a-z].*?', 'В пароле должна быть хотя бы одна строчная буква.'),
    (r'.*?[#?!@$%^&*-].*?', 'В пароле должен быть хотя бы один спецсимвол.'),
)


def validate_username(username):
    if not re.fullmatch(USERNAME_REGEX, username):
        raise ValidationError('В Username неподходящие символы.')
    if username in settings.USERNAME_BLACKLIST:
        raise ValidationError(
            'Этот username выбрать нельзя, попробуйте другой.'
        )


def validate_email(email):
    if not re.fullmatch(EMAIL_REGEX, email):
        raise ValidationError('В E-Mail ошибка, исправьте.')


def validate_password(password):
    for regex, msg in PASSWORD_REGEXES:
        if not re.fullmatch(regex, password):
            raise ValidationError(msg)

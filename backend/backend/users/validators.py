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
NAME_REGEX = r'^[a-zA-Zа-яА-Я-]+$'


def validate_username(username):
    if not re.fullmatch(USERNAME_REGEX, username):
        raise ValidationError('В username неподходящие символы.')
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


def validate_name(name):
    if not re.fullmatch(NAME_REGEX, name):
        raise ValidationError('Имя должно быть одним словом.')

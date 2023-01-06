from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_username, validate_email, validate_password


class User(AbstractUser):
    username = models.CharField(
        'Username',
        max_length=settings.LONG_FIELD,
        unique=True,
        help_text=('Required. 150 characters or fewer. Letters, digits'
                   'and @/./+/-/_ only.'),
        blank=False,
        validators=[validate_username]
    )
    email = models.EmailField(
        'E-Mail',
        max_length=settings.EMAIL_FIELD,
        blank=False,
        unique=True,
        validators=[validate_email])
    first_name = models.CharField('First Name', max_length=settings.LONG_FIELD,
                                  blank=False)
    last_name = models.CharField('Last Name', max_length=settings.LONG_FIELD,
                                 blank=False)
    password = models.CharField('Password', max_length=settings.BIT_7_FIELD,
                                blank=False, validators=[validate_password])

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reader',
        verbose_name='Читатель',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author',
        verbose_name='Автор',
    )

    def __str__(self):
        return f'{self.user} подписан на {self.author}'

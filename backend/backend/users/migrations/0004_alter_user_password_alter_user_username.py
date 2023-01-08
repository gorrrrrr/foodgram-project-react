# Generated by Django 4.1 on 2023-01-06 19:01

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(help_text='До 128 символов. Заглавные, строчные буквы, цифры и спецсимволы должны использоваться хотя бы раз.', max_length=128, validators=[users.validators.validate_password], verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='До 150 символов. Используйте буквы, цифры и спецсимволы.', max_length=150, unique=True, validators=[users.validators.validate_username], verbose_name='Username'),
        ),
    ]

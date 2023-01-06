# Generated by Django 4.1 on 2023-01-05 17:36

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[users.validators.validate_email], verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Required. 150 characters or fewer. Letters, digitsand @/./+/-/_ only.', max_length=150, unique=True, validators=[users.validators.validate_username], verbose_name='Username'),
        ),
    ]

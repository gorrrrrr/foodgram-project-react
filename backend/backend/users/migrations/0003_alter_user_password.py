# Generated by Django 4.1 on 2023-01-06 14:30

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, validators=[users.validators.validate_password], verbose_name='Password'),
        ),
    ]
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.validators import validate_password

User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    password = serializers.CharField(style={"input_type": "password"},
                                     write_only=True,
                                     validators=[validate_password])

    class Meta(UserCreateSerializer.Meta):
        fields = ('email', 'id', 'username', 'first_name',
                  'last_name', 'password')  # is_subscribed

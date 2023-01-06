from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        # Remove the confirm_password field from the validated data
        del validated_data['confirm_password']
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, required=False)
    username = serializers.CharField(max_length=255, required=False)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password')
        print("seri")
        if email is None and username is None:
            raise ValidationError('An email or username is required to log in.')

        user = None
        if email is not None:
            user = User.objects.filter(email=email).first()
        elif username is not None:
            user = User.objects.filter(username=username).first()

        if user is not None:
            if not user.check_password(password):
                raise ValidationError('Incorrect password')
        else:
            raise ValidationError('User not found')

        return {
            'user': user,
            'token': user.auth_token
            }

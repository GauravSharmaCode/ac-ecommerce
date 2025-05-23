from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        """
        Validate that the provided username is not already taken.

        Args:
            value (str): The username to validate.

        Raises:
            serializers.ValidationError: If the username is already taken.

        Returns:
            str: The validated username.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value

    def validate_email(self, value):
        """
        Validate that the provided email is not already registered.

        Args:
            value (str): The email to validate.

        Raises:
            serializers.ValidationError: If the email is already registered.

        Returns:
            str: The validated email.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    def create(self, validated_data):
        """
        Creates and returns a new user instance using the provided validated data.

        Args:
            validated_data (dict): A dictionary containing validated user data,
                which includes 'username', 'email', and 'password'.

        Returns:
            User: A newly created User instance.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
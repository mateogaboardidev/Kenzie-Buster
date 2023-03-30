from rest_framework import serializers, validators
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        required=True,
        validators=[
            validators.UniqueValidator(User.objects.all(), "username already taken.")
        ],
    )
    email = serializers.EmailField(
        required=True,
        validators=[
            validators.UniqueValidator(User.objects.all(), "email already registered.")
        ],
    )
    birthdate = serializers.DateField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    is_employee = serializers.BooleanField(required=False)
    is_superuser = serializers.SerializerMethodField()

    def get_is_superuser(self, user: User):
        return user.is_employee

    def create(self, validated_data: dict):

        if validated_data.get("is_employee"):
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict):
        hash_password = validated_data.get("password", instance.password)

        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.set_password(hash_password)
        instance.birthdate = validated_data.get("birthdate", instance.birthdate)

        instance.save()

        return instance

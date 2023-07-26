from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(max_length=150, validators=[UniqueValidator(queryset=User.objects.all(),message="username already taken.")])
    email = serializers.CharField(max_length=127, validators=[UniqueValidator(queryset=User.objects.all(),message="email already registered.")])
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)

    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data:dict)->User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        
        return User.objects.create_user(**validated_data) 
    
    def update(self, instance:User, validated_data:dict)->User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


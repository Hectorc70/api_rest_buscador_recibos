  
from rest_framework.validators import UniqueTogetherValidator

from rest_framework import serializers
from user.models import NewUser


class UserSerializer(serializers.ModelSerializer):
    def create(self, validate_data):
        user = NewUser.objects.create(**validate_data)

        return user


    class Meta:
        model = NewUser
        fields = ('control','is_staff')

        validators = [
            UniqueTogetherValidator(
                queryset = NewUser.objects.all(),
                fields=['control']
            )
        ]



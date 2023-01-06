from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'username']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        print("####>", validated_data)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        print(instance)
        if password is not None:
            instance.set_password(password)
        instance.save()
        print("instance->", instance)
        return instance

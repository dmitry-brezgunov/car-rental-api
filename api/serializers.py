from rental.models import Car, Language, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'lang', 'password', )
        write_only_fields = ('password', )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CarSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'name', 'creation_year', 'created_at', )

    def get_name(self, obj):
        request = self.context.get('request')
        if request.user.lang == Language.RU:
            return obj.name_ru
        return obj.name_en


from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.http import HttpResponse

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        active_user_id = self.context['request'].user.id
        if not active_user_id:
            raise ValidationError("You must sign in to post an advertisement")
        active_user_open_ads = Advertisement.objects.filter(creator_id=active_user_id, status='OPEN')
        if self.context['request'].method == 'POST' and active_user_open_ads.count() >= 10:
            raise ValidationError("You can't have more than 10 opened advertisements")
        elif self.context['request'].method == 'PATCH' and \
                active_user_open_ads.count() >= 10 and data['status'] == 'OPEN':
            raise ValidationError("You can't have more than 10 opened advertisements")
        return data


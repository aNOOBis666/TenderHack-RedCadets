from rest_framework import serializers

from .models import Deal


class DealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['id_deal', 'name_deal', 'description_deal', 'date_deal', 'owner_id', 'first_id', 'second_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ['role']

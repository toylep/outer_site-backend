from rest_framework import serializers
from partner.models import Document,Partner
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class DocumentSerializer(serializers.ModelSerializer):

    file = serializers.FileField()
    class Meta:
        model = Document
        fields = [
            'id',
            'name',
            'file',
        ]


class PartnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Partner
        fields = '__all__'



from rest_framework import serializers
from .models import Wallet
from django.contrib.auth.models import User

class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        depth = 2
        fields = ['pk', 'name', 'user', 'companies']

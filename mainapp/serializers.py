from rest_framework import serializers
from .models import APIKEY



class APIKEYSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKEY
        fields = ['key', 'length']

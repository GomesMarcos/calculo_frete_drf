from rest_framework import serializers
from .models import *


class TransportadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

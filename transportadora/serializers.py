from rest_framework import serializers
from .models import *
from produto.models import Produto


class TransportadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportadora
        fields = '__all__'

from rest_framework import serializers
from .models import *


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Object
        fields = ['nome', 'peso', 'dimensoes']

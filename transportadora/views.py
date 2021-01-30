from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from .serializers import TransportadoraSerializer
from .models import Transportadora
from produto.models import Produto


class TransportadoraViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para Transportadoras
    """
    queryset = Transportadora.objects.all()
    serializer_class = TransportadoraSerializer

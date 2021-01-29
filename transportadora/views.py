from rest_framework import viewsets
from .serializers import TransportadoraSerializer

from .models import Object


class TransportadoraViewSet(viewsets.ModelViewSet):
    """ 
    Endgpoint da API para Transportadoras
    """
    queryset = Object.objects.all()
    serializer_class = TransportadoraSerializer

from rest_framework import viewsets
from .serializers import ProdutoSerializer

from .models import Object


class ProdutoViewSet(viewsets.ModelViewSet):
    """ 
    Endgpoint da API para Produtos
    """
    queryset = Object.objects.all()
    serializer_class = ProdutoSerializer

from rest_framework import viewsets
from .models import Object
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    """ 
    Endgpoint da API para Produtos
    """
    queryset = Object.objects.all()
    serializer_class = ProdutoSerializer

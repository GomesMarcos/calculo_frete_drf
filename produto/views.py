from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProdutoSerializer
from .models import Produto
from transportadora.models import Transportadora


class ProdutoViewSet(viewsets.ModelViewSet):
    """ 
    Endpoint da API para Produtos
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


@api_view(['GET'])
def montar_dados_frete(request, pk):
    """
    Função responsável por montar a lista de fretes compatível
    com as dimensões do produto

    Args:
        request (rest_framework.request.Request): Requisição feita à API
        pk (int): identificador do para o objeto "Produto"

    Returns:
        frete_list(list): Lista com os objetos serializados informando os dados para o frete
    """

    transportadoras = Transportadora.objects.all()
    frete_list = list()

    print('\n\n\n', type(request), type(pk), '\n\n\n')

    produto = Produto.objects.filter(id=pk).values()

    for transportadora in transportadoras:
        if validar_parametros_frete(produto, transportadora):
            frete_list.append(dict({
                'nome': transportadora.nome,
                'valor_frete': (produto[0]['peso'] * transportadora.constante_para_calculo_de_frete) / 10,
                'prazo_dias': transportadora.prazo_entrega
            }))

    return Response(frete_list)


def validar_parametros_frete(produto, transportadora):
    """
    Valida se o produto é apto ou não a ser inserido
    na lista de fretes de acordo com as dimensões mínimas e máximas
    dadas pela transportadora

    Args:
        produto (QuerySet): [description]
        transportadora (QuerySet): [description]

    Returns:
        bool: Caso as dimensões do produto estejam dentro dos parâmetros da transportadora, True
    """
    if produto[0]['dimensoes']['altura'] < transportadora.altura_minima:
        return False
    if produto[0]['dimensoes']['altura'] > transportadora.altura_maxima:
        return False
    if produto[0]['dimensoes']['largura'] < transportadora.largura_minima:
        return False
    if produto[0]['dimensoes']['largura'] > transportadora.largura_maxima:
        return False

    return True

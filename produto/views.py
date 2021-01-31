from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from transportadora.models import Transportadora
from .serializers import ProdutoSerializer
from .models import Produto
from .validations import *


class ProdutoViewSet(viewsets.ModelViewSet):
    """ 
    Endpoint da API para Produtos
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


@api_view(['GET', 'POST'])
def montar_dados_frete(request, pk=None):
    """
    Função responsável por montar a lista de fretes compatível
    com as dimensões do produto

    Args:
        request (rest_framework.request.Request): Requisição feita à API
        pk (int): identificador do para o objeto "Produto",
            caso esteja consultando um produto cadastrado no painel administrativo

    Returns:
        frete_list (list): Lista com os objetos serializados informando os dados para o frete
    """

    transportadoras = Transportadora.objects.all()
    frete_list = list()
    status_validacao_produto = True

    # Validando se o produto é oriundo do banco de dados ou do teste da API
    if pk == None:
        produto = request.data
    else:
        produto = Produto.objects.filter(id=pk).values()[0]

    # Caso esteja acessando http://127.0.0.1:8000/api/v1/frete pelo navegador
    if produto == {} and request.method == 'GET':
        mensagem = 'Olá! Espero que você se divita testando essa API feita com muito carinho e café. =)'
        return Response({'msg': mensagem}, status=status.HTTP_200_OK)

    # Validando produto
    validacao_produto = validar_produto(produto)
    status_validacao_produto = validacao_produto['status']
    if 'msg' in validacao_produto:
        mensagem = validacao_produto['msg']

    if not produto == {} and validacao_produto['status'] == True:
        for transportadora in transportadoras:
            if validar_parametros_frete(produto, transportadora) == True:
                frete_list.append(dict({
                    'nome': transportadora.nome,
                    'valor_frete': (produto['peso'] * transportadora.constante_para_calculo_de_frete) / 10,
                    'prazo_dias': transportadora.prazo_entrega
                }))
        return Response(frete_list)

    else:
        return Response({'msg': mensagem}, status=status.HTTP_400_BAD_REQUEST)

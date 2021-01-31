def validar_parametros_frete(produto, transportadora):
    """
    Valida se os dados do POST são válidos, ou não, para o
    cálculo de frete de acordo com as dimensões mínimas e máximas
    informadas pelas transportadoras cadastradas

    Args:
        produto (dict)
        transportadora (QuerySet)

    Returns:
        bool: Caso as dimensões do produto estejam dentro dos parâmetros da transportadora, True
    """
    if produto['dimensao']['altura'] < transportadora.altura_minima:
        return False
    if produto['dimensao']['altura'] > transportadora.altura_maxima:
        return False
    if produto['dimensao']['largura'] < transportadora.largura_minima:
        return False
    if produto['dimensao']['largura'] > transportadora.largura_maxima:
        return False

    return True


def validar_produto(produto):
    """
    Verifica se o produto possuo as chaves:
    ['dimensao']['altura'],
    ['dimensao']['largura'] e
    ['peso'],
    para que se possa calcular o frete com esses valores


    Args:
        produto (dict)

    Returns:
        validacao (dict): Retorna um dicionário contendo "msg", caso haja erro, e o status da validação
    """

    validacao = {
        'status': True
    }

    # Validando Chaves de produto
    if not 'dimensao' in produto:
        validacao = {
            'msg': 'parâmetro "dimensao" não encontrado',
            'status': False
        }
    if 'dimensao' in produto and not 'altura' in produto['dimensao']:
        validacao = {
            'msg': validacao['msg'] + ' parâmetro "altura" não encontrado',
            'status': False
        }

    if 'dimensao' in produto and not 'largura' in produto['dimensao']:
        validacao = {
            'msg': validacao['msg'] + ' parâmetro "largura" não encontrado',
            'status': False
        }

    if not 'peso' in produto:
        validacao = {
            'msg': validacao['msg'] + ' parâmetro "peso" não encontrado',
            'status': False
        }

    """
    Caso o JSON esteja montado com as chaves erradas
    este método não validará seus respectivos valores.
    """
    if validacao['status'] == False:
        return validacao

    # Validando Valores das Chaves de produto
    if not type(produto['dimensao']['altura']) == int:
        validacao = {
            'msg': validacao['msg'] + ' altura precisa ter um valor inteiro',
            'status': False
        }
    if not type(produto['dimensao']['largura']) == int:
        validacao = {
            'msg': validacao['msg'] + ' largura precisa ter um valor inteiro',
            'status': False
        }
    if not type(produto['peso']) == int:
        validacao = {
            'msg': validacao['msg'] + ' peso precisa ter um valor inteiro',
            'status': False
        }

    return validacao

# Cálculo de Frete Baseado em Medidas

## Executando o proheto

Para montagem e execução do do projeto, foram criados alguns scrips personalizados.
Seguem passos abaixo:

### Dependências

- Python 3.x
- virtualenv / venv / pipenv

### Criação do ambiente virtual e setup do projeto (Linux / Mac)

- `virtualenv venv`
- `source ./script_activate.sh`
- `python manage.py createsuperuser --email <user_email> --username <user_name>` subistitua os nomes entre <> pelos respectivos valores
- `pip install -r requirements.txt`
- `./runserver`

### Testando a API

A API Root está disponível, por padrão, [aqui](http://127.0.0.1:8000/api/v1/)
O link para consulta de frete está disponível [aqui](http://127.0.0.1:8000/api/v1/produtos/1/frete), onde o número corresponde ao id do produto requisitando o frete

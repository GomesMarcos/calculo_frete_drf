"""calculo_frete URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from produto.views import ProdutoViewSet, montar_dados_frete
from transportadora.views import TransportadoraViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)
router.register(r'transportadoras', TransportadoraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/produtos/<int:pk>/frete', montar_dados_frete),
]

"""calculo_frete URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from produto.views import ProdutoViewSet

router = routers.DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]

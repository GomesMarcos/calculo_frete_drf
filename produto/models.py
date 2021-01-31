from django.db import models
from django.utils.translation import gettext_lazy as _
from transportadora.models import Transportadora


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(decimal_places=2, max_digits=999)
    peso = models.PositiveSmallIntegerField()
    dimensao = models.JSONField(default=dict)

    class Meta:
        verbose_name = _('produto')
        verbose_name_plural = _('produtos')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("produto_detail", kwargs={"pk": self.pk})

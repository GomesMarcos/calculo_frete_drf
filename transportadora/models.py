from django.db import models
from django.utils.translation import gettext_lazy as _


class Object(models.Model):
    nome = models.CharField(max_length=50)
    constante_para_calculo_de_frete = models.DecimalField(
        decimal_places=1, max_digits=2)
    altura_minima = models.PositiveSmallIntegerField()
    altura_maxima = models.PositiveSmallIntegerField()
    largura_minima = models.PositiveSmallIntegerField()
    largura_maxima = models.PositiveSmallIntegerField()
    prazo_entrega = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = _('Transportadora')
        verbose_name_plural = _('Transportadoras')

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("transportadora_detail", kwargs={"pk": self.pk})

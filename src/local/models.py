from django.db import models

# Create your models here.
from django.db import models


class Local(models.Model):
    nome = models.CharField(max_length=255)
    numero_de_vagas = models.PositiveIntegerField()
    imagens = models.ImageField(upload_to='local/imagens/', blank=True, null=True)
    localizacao = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.nome

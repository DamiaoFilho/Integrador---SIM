from django.db import models

# Create your models here.


class Instrument(models.Model):
    image = models.ImageField(upload_to="instruments/images", verbose_name="Imagem")
    name = models.CharField(max_length=150, verbose_name="Nome")
    model = models.CharField(max_length=150, verbose_name="Modelo")
    brand = models.CharField(max_length=150, verbose_name="Marca")
    serial_number = models.IntegerField(verbose_name="Número de série")
    color = models.CharField(verbose_name="Cor")
    condition = models.TextField(verbose_name="Condição")
    status = models.BooleanField(default=True, verbose_name="Disponibilidade")


    def __str__(self) -> str:
        return self.name
    
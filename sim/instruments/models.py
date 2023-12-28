from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Instrument(models.Model):
    image = models.ImageField(upload_to="instruments/images", verbose_name="Imagem")
    name = models.CharField(max_length=150, verbose_name="Nome")
    model = models.CharField(max_length=150, verbose_name="Modelo")
    brand = models.CharField(max_length=150, verbose_name="Marca")
    serial_number = models.IntegerField(verbose_name="Número de série")
    color = models.CharField(verbose_name="Cor")
    condition = models.TextField(verbose_name="Condição")
    status = models.BooleanField(default=True, verbose_name="Disponibilidade")
    category = models.ManyToManyField(Category, verbose_name="Categoria", blank=True)
    type = models.ManyToManyField("InstrumentType", verbose_name="Tipo", blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Instrumento"
        verbose_name_plural = "Instrumentos"


class InstrumentType(models.Model):
    name = models.CharField(verbose_name="Nome")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Tipo de Instrumento"
        verbose_name_plural = "Tipos de Instrumentos"
from django.db import models
from ..instruments.models import Instrument
from ..users.models import User
# Create your models here.
class Lending(models.Model):
    instrument = models.OneToOneField(Instrument, on_delete=models.CASCADE, verbose_name="Instrumento")
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student", verbose_name="Estudante")
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="professor", verbose_name="Professor")
    initDate = models.DateField(verbose_name="Data de Início")
    finalDate = models.DateField(verbose_name="Data de Fim")

    def __str__(self) -> str:
        return f"{self.student.name}: {self.instrument}"
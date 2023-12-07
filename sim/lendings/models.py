from django.db import models
from ..instruments.models import Instrument
from ..users.models import User, Student, Professor
# Create your models here.

class Lending(models.Model):

    class StatusChoices(models.TextChoices):
        IN_PROGRESS = ("IN_PROGRESS", "Em andamento")
        IN_ANALISYS = ("IN_ANALISYS", "Em análise")
        DENIED = ("DENIED", "Indeferida")
        FINISHED = ("FINISHED", "Finalizado")

    initDate = models.DateField(verbose_name="Data de Início")
    finalDate = models.DateField(verbose_name="Data de Fim")
    justify = models.TextField(verbose_name="Justificativa")
    status = models.CharField(verbose_name="Status", choices=StatusChoices.choices)

    instrument = models.OneToOneField(Instrument, on_delete=models.CASCADE, verbose_name="Instrumento")
    professor = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="professor", verbose_name="Professor")
    student = models.OneToOneField(Professor, on_delete=models.CASCADE, related_name="student", verbose_name="Estudante")

    def __str__(self) -> str:
        return f"{self.student.name}: {self.instrument}"
    

class Return(models.Model):
    date = models.DateField(verbose_name="Data de Devolução")
    photo = models.ImageField(upload_to="media/returns/", verbose_name="Foto de devolução")
    commentary = models.TextField(verbose_name="Observações")
    lending = models.OneToOneField(Lending, on_delete=models.CASCADE)
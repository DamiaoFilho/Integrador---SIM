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
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    justify = models.TextField(verbose_name="Justificativa")
    status = models.CharField(verbose_name="Status", choices=StatusChoices.choices, default=StatusChoices.IN_ANALISYS)

    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, verbose_name="Instrumento")
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="professor", verbose_name="Professor", blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student", verbose_name="Estudante")

    def __str__(self) -> str:
        return f"{self.student.user.username}: {self.instrument}"
    

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
    

class Return(models.Model):
    date = models.DateField(verbose_name="Data de Devolução")
    photo = models.ImageField(upload_to="media/returns/", verbose_name="Foto de devolução", blank=True, null=True)
    commentary = models.TextField(verbose_name="Observações")
    lending = models.OneToOneField(Lending, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.lending.student.user.username}: {self.lending.instrument.name}"
    
    class Meta:
        verbose_name = "Devolução"
        verbose_name_plural = "Devoluções"


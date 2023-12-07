from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

class User(AbstractUser):
    """
    Default custom user model for SIM.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    



class Profile(models.Model):

    class Meta:
        abstract = True

    register = models.IntegerField(verbose_name="Matrícula")
    photo = models.ImageField(verbose_name="Foto de Perfil", blank=True, default='default/profiles/profile.webp')
    phone = models.CharField(verbose_name="Telefone")


class Student(Profile):

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudantes"

    class YearChoices(models.TextChoices):
        ONE = ("ONE", "1º Ano")
        TWO = ("TWO", "2º Ano")
        THREE = ("THREE", "3º Ano")
        FOUR = ("FOUR", "4º Ano")
    
    class CoursesChoices(models.TextChoices):
        API = ("API", "Apicultura")
        ALI = ("ALI", "Alimentos")
        INFO = ("INFO", "Informática")
        ADS = ("ADS", "Análise e Desenvolvimento de Sistemas")
        QUI = ("QUI", "Química")
        AGRO = ("AGRO", "Agroindústria")

    class ShiftChoices(models.TextChoices):
        MAT = ("MAT", "Matutino")
        VESP = ("VESP", "Vespertino")
        NOT = ("NOT", "Noturno")

    year = models.CharField(verbose_name="Ano", choices=YearChoices.choices)
    course = models.CharField(verbose_name="Curso", choices=CoursesChoices.choices)
    shift = models.CharField(verbose_name="Turno", choices=ShiftChoices.choices)
    is_colleger = models.BooleanField(default=False)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="StudentUser")

    def __str__(self) -> str:
        return self.user.username
    
class Professor(Profile):
    employee_register = models.IntegerField(verbose_name="Número de Servidor")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ProfessorUser")
    
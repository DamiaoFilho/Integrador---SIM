from django.db import models

# Create your models here.


class Instrument(models.Model):
    image = models.ImageField(upload_to="instruments/images")
    name = models.CharField(max_length=150)
    modelo = models.CharField(max_length=150)
    serial_number = models.IntegerField()
    color = models.CharField()
    condition = models.TextField()
    status = models.BooleanField()
    
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
# Create your models here.

class ObjetiosUsuario(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    edad = models.IntegerField()
    peso_actual_kilogramos = models.FloatField()
    peso_objetivo_kilogramos = models.FloatField()


    def __str__(self):
        return f"{self.edad} {self.peso_actual_kilogramos} {self.peso_objetivo_kilogramos}"



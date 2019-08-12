from django.db import models
from modules.bases.Model.ClassModel import ClassModel


class BasesManager(models.Manager):
    pass


class Categoria(ClassModel):
    descripcion = models.CharField(
        max_length=100, help_text='Descripcion de la categoria', unique=True)
    objects = BasesManager()

    def __str__(self):
        return self.descripcion

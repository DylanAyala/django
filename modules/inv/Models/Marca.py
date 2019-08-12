from django.db import models
from modules.bases.Model.ClassModel import ClassModel


class Marca(ClassModel):
    descripcion = models.CharField(
        max_length=100, help_text='Descripcion de la Marca', unique=True)

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = "Marca"

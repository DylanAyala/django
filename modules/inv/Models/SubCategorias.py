from django.db import models
from modules.bases.Model.ClassModel import ClassModel
from modules.inv.Models.Categoria import Categoria


class SubCategoria(ClassModel):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Categoria',
        unique=True
    )

    def __str__(self):
        return self.descripcion

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')

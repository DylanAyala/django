from django.db import models
from django.contrib.auth.models import User


class ClassModel(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=False)
    un = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

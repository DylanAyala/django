from django import forms
from ..Models.Categoria import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado', ]
        labels = {'descripcion': 'Descripcion de la Categoria', 'estado': 'Estado'}
        widget = {"descripcion", forms.TextInput}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attr.update({
                    "class": "form-control"
                })

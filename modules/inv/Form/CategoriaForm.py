from django import forms
from modules.inv.Models.Categoria import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado', ]
        labels = {'descripcion': 'Descripcion de la Categoria',
                  'estado': 'Estado'}
        widget = {"descripcion", forms.TextInput,
                  "estado", forms.CheckboxInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == "estado":
                self.fields[field].widget.attrs.update({
                    "class": "form-check-input"
                })
            else:
                self.fields[field].widget.attrs.update({
                    "class": "form-control"
                })

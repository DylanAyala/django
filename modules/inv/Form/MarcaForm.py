from django import forms
from modules.inv.Models.Marca import Marca


class MarcaForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=100, label="Descripcion")

    class Meta:
        model = Marca
        fields = ['descripcion', 'estado', ]
        labels = {'descripcion': 'Descripcion de la Marca',
                  'estado': 'Estado'}
        widget = {"descripcion", forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })

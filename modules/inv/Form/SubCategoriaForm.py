from django import forms
from modules.inv.Models.SubCategorias import SubCategoria
from modules.inv.Models.Categoria import Categoria


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.filter(estado=True)
                                       .order_by('descripcion'))

    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado', ]
        labels = {'descripcion': 'Descripcion de la SubCategoria',
                  'estado': 'Estado'}
        widget = {"descripcion", forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })
        self.fields['categoria'].empty_label = "Selecciones un categoria"

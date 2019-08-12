from modules.inv.Models.Marca import Marca
from modules.inv.Form.MarcaForm import MarcaForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "base:login"


class MarcaNew(LoginRequiredMixin, generic.CreateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaDel(LoginRequiredMixin, generic.DeleteView):
    model = Marca
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:marca_list')

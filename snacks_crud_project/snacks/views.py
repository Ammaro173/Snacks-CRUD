from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Snack

# Create your views here.


class HomeView(TemplateView):
    model = Snack
    template_name = "home.html"


class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"


class SnackDetailView(DetailView):
    model = Snack
    template_name = "snack_detail.html"


class SnackCreateView(CreateView):
    model = Snack
    template_name = "snack_create.html"
    fields = ["title", "purchaser", "description"]


class SnackUpdateView(UpdateView):
    model = Snack
    template_name = "snack_update.html"
    fields = ["title", "purchaser", "description"]


class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "snack_delete.html"
    success_url = "/admin/snacks/snack/"

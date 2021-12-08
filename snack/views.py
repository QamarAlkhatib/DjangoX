# from django.db import models
from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Snacks


class SnacksListView(ListView):
    template_name = "snack/snack_list.html"
    model = Snacks


class SnacksDetailView(DetailView):
    template_name = "snack/snack_detail.html"
    model = Snacks


class SnacksCreateView(CreateView):
    template_name = "snack/snack_create.html"
    model = Snacks
    fields = []


class SnacksUpdateView(UpdateView):
    template_name = "snack/snack_update.html"
    model = Snacks
    fields = []


class SnacksDeleteView(DeleteView):
    template_name = "snack/snack_confirm_delete.html"
    model = Snacks
    success_url = reverse_lazy("_list") 
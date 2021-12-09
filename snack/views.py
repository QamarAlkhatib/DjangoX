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
    template_name = "snacks/snack_list.html"
    model = Snacks


class SnacksDetailView(DetailView):
    template_name = "snacks/snack_detail.html"
    model = Snacks


class SnacksCreateView(CreateView):
    template_name = "snacks/snack_create.html"
    model = Snacks
    fields = ['title', 'purchaser', 'description']



class SnacksUpdateView(UpdateView):
    template_name = "snacks/snack_update.html"
    model = Snacks
    fields = ['title', 'purchaser', 'description']


class SnacksDeleteView(DeleteView):
    template_name = "snacks/snack_confirm_delete.html"
    model = Snacks
    success_url = reverse_lazy("snack_list") 
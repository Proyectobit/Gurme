from django.shortcuts import render
from django.views.generic import ListView
from chefs.models import Chef


class ChefsListView(ListView):
    model = Chef
    template_name = "chef_list.html"

from django.shortcuts import render
from .models import Link
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse_lazy
# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "links/index.html"

class LinksListView(ListView):
    model = Link
    template_name = "links/links.html"


class LinksDetailView(DetailView):
    model = Link
    template_name = "links/links_detail.html"


class LinksCreateView(CreateView):
    model = Link
    template_name = "links/link_update.html"
    fields = ["name", "url", "category"]
    success_url = reverse_lazy("links")

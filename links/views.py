from django.shortcuts import render
from .models import Link
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
# Create your views here.

# def links(request):
#     links = Link.objects.all()
#     context = {'links': links }
#     return render(request, 'links/links.html', context)

class LinksListView(ListView):
    model = Link
    template_name = "links.html"

class LinksDetailView(DetailView):
    model = Link
    template_name = "links_detail.html"
class LinksCreateView(CreateView):
    model = Link
    template_name = "link_update.html"
    fields = ["name", "url", "category"]
    success_url = reverse_lazy("links")

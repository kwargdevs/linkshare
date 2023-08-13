# imports

from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    TemplateView
)
from django.urls import reverse_lazy
from django.http import HttpRequest
from django.db.models import QuerySet
from django.contrib.auth.decorators import login_required

from .models import Link, Category


class IndexTemplateView(TemplateView):
    template_name = "links/index.html"


class LinksListView(ListView):
    model = Link
    template_name = "links/links.html"


class LinksDetailView(DetailView):
    model = Link
    template_name = "links/links_detail.html"


""" Old link create view. Remove if new link create view works as expected."""
#class LinksCreateView(CreateView):
#    model = Link
#    template_name = "links/link_update.html"
#    fields = ["name", "url", "category"]
#    success_url = reverse_lazy("links")


@login_required
def links_create_view(request: HttpRequest):
    """
    View for link creation
    """
    
    tags: QuerySet = Category.objects.all()
    
    # handle post request
    if request.method == "POST":
        _, title, tag, url, description = request.POST.values() # unpack request data
        
        # get a category if it already exists or create a new one
        category: Category = Category.objects.get_or_create(name=tag)[0]
        
        link: Link = Link.objects.get_or_create(
            name=title, category=category, url=url, description=description
        )[0]
        
        link.save()
        return redirect("links:links")
        
    return render(request, "links/link_create.html", {"tags": tags})

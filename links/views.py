from django.shortcuts import render
from .models import Link
# Create your views here.

def links(request):
    links = Link.objects.all()
    context = {'links': links }
    return render(request, 'links/links.html', context)

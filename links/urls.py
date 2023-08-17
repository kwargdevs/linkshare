from django.urls import path
from .views import (
    LinksListView,
    #LinksCreateView, Old link create view
    LinksDetailView,
    IndexTemplateView,
    links_create_view
)

app_name = "links"

urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    # path("links/create/", LinksCreateView.as_view(), name="link_create"),
    path("links/create/", links_create_view, name="link_create"), # new
    path("links/<int:pk>", LinksDetailView.as_view(), name="link_detail"),
    path("links/", LinksListView.as_view(), name="links"),
]

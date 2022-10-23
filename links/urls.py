from django.urls import path
from .views import LinksListView, LinksCreateView, LinksDetailView

app_name = "links"

urlpatterns = [
    path("links/create/", LinksCreateView.as_view(), name="link_create"),
    path("links/<int:pk>", LinksDetailView.as_view(), name="link_detail"),
    path("links", LinksListView.as_view(), name="links"),
]

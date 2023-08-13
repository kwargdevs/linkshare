from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    description = models.TextField(default="")
    
    def get_absolute_url(self):
        return reverse("links:link_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

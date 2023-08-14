from django.contrib import admin
from .models import Link, Tag, LinkComment


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    """
    Link model admin descriptor
    """
    
    list_display = ("tag", "url","submitter", "date_added")
    list_filter = ("tag", "votes", "date_added")
    search_fields = ("tag", "url", "date_added")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Tag model admin descriptor
    """
    
    list_display = ("name", "date_created")
    list_filter = ("name", "date_created")
    search_fields = ("name",)
    

@admin.register(LinkComment)
class LinkCommentAdmin(admin.ModelAdmin):
    """
    LinkComment model admin descriptor
    """
    
    list_display = ("link", "comment", "date_created")
    list_filter = ("link", "date_created")

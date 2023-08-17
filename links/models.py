from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# User object

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["name"], name="name_index")
        ]

    def __str__(self):
        return self.name


class Link(models.Model):
    """
    For upvote and downvote, use thw following code snippet
    >>> instance.votes.add(user) # single upvote
    >>> instance.votes.add(user1, user2, user3) # multiple upvotes
    
    >>> instance.votes.remove(user) # single downvote
    >>> instance.votes.add(user1, user2, user3) # multiple downvotes
    """
    
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=500)   
    tag = models.ForeignKey(Tag, default=None, on_delete=models.CASCADE)
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploader")
    description = models.TextField(default="")
    votes = models.ManyToManyField(User)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=["title", "url", "tag"], name="main_idxs"),
            models.Index(fields=["description"], name="sub_idxs")
        ]
    
    def get_absolute_url(self):
        return reverse("links:link_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class LinkComment(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment

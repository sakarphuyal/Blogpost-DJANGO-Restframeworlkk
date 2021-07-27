from typing import ContextManager
from typing_extensions import Concatenate
from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField (max_length=300)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to="images/", default="images/default.png")


    def get_absolute_url(self):
        return reverse("blog:single", args=[self.slug])

    def __str__(self):
        return self.title 

    def __str__(self):
        return self.content

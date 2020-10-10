from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post (models.Model):
    STATUS = (
        ('draft','draft'), #rascunho
        ('published','published'), #publicado
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) #salvar data 1 vez quando criar
    Changed = models.DateTimeField(auto_now=True) #salvar data todo vez que alterar
    status = models.CharField(max_length=10, choices=STATUS, default='rascunho')

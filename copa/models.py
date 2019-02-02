from django.db import models
from django.utils import timezone


class Post(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return f'{self.nome} ({self.quantidade})'
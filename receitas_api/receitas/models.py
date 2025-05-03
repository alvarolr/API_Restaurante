from django.db import models

# Create your models here.

class Receita(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.JSONField(help_text="Lista com nome e quantidade dos ingredientes")
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

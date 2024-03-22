from django.db import models

# Create your models here.pdm run python manage.py makemigrations
class Categoria(models.Model):
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.descricao

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome
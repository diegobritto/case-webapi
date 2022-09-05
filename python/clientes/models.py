from django.db import models

class Cliente(models.Model):

    nome_completo = models.CharField('nome completo',blank=False,max_length=150)
    email = models.EmailField(blank=False, max_length=150, unique=True)


    def __str__(self):
        return self.email


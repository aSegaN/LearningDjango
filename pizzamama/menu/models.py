from django.db import models

# Create your models here.


class Pizza(models.Model):
    nom = models.CharField(max_length=64)
    ingredients = models.CharField(max_length=256)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

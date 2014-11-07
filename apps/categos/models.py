from django.db import models

# Create your models here.
# Categorie models

class Categorie(models.Model):
    #code
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom


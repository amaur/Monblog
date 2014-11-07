from django.db import models
from apps.categos.models import Categorie

# Create your models here.
# Article models

class Article( models.Model ):
    #code
    category = models.ForeignKey(Categorie)
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=50)
    likes=models.IntegerField(default=0)
    contenu =models.TextField(null=True)
    date=models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name="Date de parution")
    
    def __str__(self):
        return self.titre 


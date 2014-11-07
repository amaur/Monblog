from django.db import models
from apps.artigos.models import Article

# Create your models here.
# comentaire models

class Commentaire(models.Model):
    #code
    comentair=models.TextField(max_length=200)
    arti = models.ForeignKey(Article)
    likis= models.IntegerField(default=0)
    def __str__(self):
        return self.comentair 
    


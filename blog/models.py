from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone

class Auteur(models.Model):
    nom_complet = models.CharField(max_length=100)
    date_naissance = models.DateField("Date de naissance")
    pays = CountryField()

    def __str__(self):
        return self.nom_complet

    @property
    def age(self):
        import datetime
        age = datetime.date() - self.date_naissance
        return age

# Création du model Article
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.CharField(max_length=255)
    date_publication = models.DateTimeField("Date de publication")
    auteur_id = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    image = models.ImageField("Image")

    def __str__(self):
        return self.titre

from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os

from django.contrib.auth.models import User

STATUS = ((0, "brouillon" ) , (1, "publié"))

# Création du model Article
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.CharField(max_length=255)
    date_publication = models.DateTimeField("Date de publication")
    auteur = models.ForeignKey(User , on_delete= models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return self.titre

@receiver(pre_delete, sender=Article)
def delete_post_image(sender, instance, **kwargs):
    # Supprimer le fichier image associé lors de la suppression de l'article
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
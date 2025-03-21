from django.contrib import admin

from .models import Article

# Lien site pour personaliser la page d'administration
# https://dev.to/vijaysoni007/how-to-show-images-of-the-model-in-django-admin-5hk4
class ItemArticle(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'date_publication']

admin.site.register(Article, ItemArticle)

# Register your models here.

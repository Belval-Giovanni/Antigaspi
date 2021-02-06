from django.contrib import admin
from . import models

admin.site.register(models.Utilisateur)
admin.site.register(models.Question)
admin.site.register(models.Contact)
admin.site.register(models.Annonce)


from django.db import models

class Question(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    question = models.TextField(blank = False)
    reponse = models.TextField(blank = False)

class Contact(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    localisation = models.TextField(blank = False)
    email = models.EmailField( max_length=254)
    telephone = models.TextField(blank = False)

class Utilisateur(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    nom = models.CharField( max_length=75)
    prenom = models.CharField( max_length=75)
    date_de_naissance = models.DateField()
    email = models.EmailField( max_length=254)
    localisation = models.TextField()
    image = models.ImageField( upload_to='static/img')


class Annonce(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    distributeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    



from django.db import models

class Question(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    question = models.TextField(blank = False)
    reponse = models.TextField(blank = False)

    def __str__(self):
        return self.question
    

class Contact(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    localisation = models.TextField(blank = False)
    email = models.EmailField( max_length=254)
    telephone = models.TextField(blank = False)

    def __str__(self):
        return self.email
    

class Utilisateur(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    nom = models.CharField( max_length=75)
    prenom = models.CharField( max_length=75)
    date_de_naissance = models.DateField()
    email = models.EmailField( max_length=254)
    localisation = models.TextField()
    image = models.ImageField( upload_to='static/img', null = True)
    telephone = models.CharField( max_length=50,null = True)
    password = models.CharField( max_length=30 ,null = True)

    def __str__(self):
        return '{} {}'.format(self.nom,self.prenom)
    


class Annonce(models.Model):
    statut = models.BooleanField(default = True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField( auto_now=True)

    distributeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    plat = models.CharField( max_length=150 , null = True)

    def __str__(self):
        return self.plat
    
    



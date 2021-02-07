from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from . import forms
from . import models

def index(request):
    context = {
        'commentaires':models.Commentaire.objects.all()
    }
    return render(request,'pages/index.html',context)


def food(request):
    context = {
        'annonces':models.Annonce.objects.all(),
    }
    return render(request,'pages/food.html',context)


def food_details(request,id):
    context = {
        'annonce':get_object_or_404(models.Annonce,id = id)
    }
    return render(request,'pages/food-details.html',context)

def inscription(request):
    if request.method == 'POST' :
        inscription = forms.Inscription(request.POST)
        models.Utilisateur(nom = inscription.data['nom'],email = inscription.data['email'],localisation = inscription.data['adresse'],\
        prenom = inscription.data['prenom'],date_de_naissance = inscription.data['date_de_naissance'],\
        telephone = inscription.data['telephone'],password = inscription.data['password']).save()
        return render(request,'pages/connexion-complete.html',{})
        
    else:
        context = {
            'inscription':forms.Inscription()
      }
    return render(request,'pages/inscription.html',context)
    

def connexion(request):
    if request.method == 'POST':
        connexion = forms.Connexion(request.POST)
        try:
            utilisateur \
            = models.Utilisateur.objects.filter(email = connexion.data['email']).get(password = connexion.data['password'])
            return HttpResponse('Bienvenu sur votre compte')
        except :
            return HttpResponse('vous n\'avez pas de compte')
    else:
        context = {
            'connexion':forms.Connexion(),
        }
    return render(request,'pages/connexion.html',context)

def map(request):
    return render(request,'pages/map.html',{})

def annonce(request):

    if request.method == 'POST':

        try:
            publication = forms.Publication(request.POST)
            utilisateur \
            = models.Utilisateur.objects.filter(email = publication.data['email']).get(password = publication.data['password'])
            models.Annonce(distributeur = utilisateur,plat = publication.data['plat'],\
            image = 'static/img/'+ publication.data['image']).save()
            return render(request,'pages/index.html')

        except :
            return render(request,'pages/404.html')
    else:
        context = {
            'publication':forms.Publication(),
        }
    return render(request,'pages/annonce.html',context)
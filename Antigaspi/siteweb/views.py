from django.shortcuts import render
from . import forms
from . import models

def index(request):
    context = {

    }
    return render(request,'pages/index.html',context)


def food(request):
    context = {

    }
    return render(request,'pages/food.html',context)


def food_details(request):
    context = {

    }
    return render(request,'pages/food-details.html',context)

def inscription(request):
    if request.method == 'POST' :
        inscription = forms.Inscription(request.POST)
        models.Utilisateur(nom = inscription.data['nom'],email = inscription.data['email'],localisation = inscription.data['adresse'],\
        prenom = inscription.data['prenom'],date_de_naissance = inscription.data['date_de_naissance'],\
        telephone = inscription.data['telephone'],).save()
        return render(request,'pages/connexion-complete.html',{})
        
    else:
        context = {
            'inscription':forms.Inscription()
      }
    return render(request,'pages/inscription.html',context)
    

def connexion(request):
    context = {

    }
    return render(request,'pages/connexion.html',context)

def map(request):
    return render(request,'pages/map.html',{})
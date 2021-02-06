from django import forms

class Inscription(forms.Form):
    nom = forms.CharField(label = 'Nom', max_length=100, required=True)
    prenom = forms.CharField(label = 'Prenom', max_length=100, required=True)
    email = forms.EmailField(label = 'email', required=True)
    telephone = forms.CharField( required=True)
    date_de_naissance = forms.DateField(label = 'Date de naisance', required=True)
    profil = forms.ImageField(label ='Profil', required=False)
    adresse = forms.CharField( max_length=200, required=True)
    password = forms.CharField( min_length = 8,max_length=30 ,required=True)




class Connexion(forms.Form):
    email = forms.EmailField(label = 'email', required=True)
    password = forms.CharField( max_length=30, required=True)

    






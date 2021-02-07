from . import views
from django.urls import path,include


urlpatterns = [
    path('',views.index,name = 'index'),
    path('food/',views.food,name ='food'),
    path('food-details/<int:id>/',views.food_details,name = 'food-details'),
    path('inscription/',views.inscription,name = 'inscription'),
    path('connexion',views.connexion,name = 'connexion'),
    path('map/',views.map,name = 'map'),
]
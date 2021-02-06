from django.shortcuts import render

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
    context = {

    }
    return render(request,'pages/inscription.html',context)


def connexion(request):
    context = {

    }
    return render(request,'pages/connexion.html',context)

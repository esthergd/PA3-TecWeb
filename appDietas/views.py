from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from .models import Favorites

def Diet(request):
    if request.method == 'POST':

        url = "https://food-nutrition-information.p.rapidapi.com/foods/search"

        querystring = {"query": request.POST["alimento"]}

        headers = {
            'x-rapidapi-host': "food-nutrition-information.p.rapidapi.com",
            'x-rapidapi-key': "5dc8a618c5msh4ef8167e50b8d14p183fa9jsn573f8dbba635"
            }

        alimentos = requests.request("GET", url, headers=headers, params=querystring).json()
        return render(request, 'diet.html', {'alimentos': alimentos["foods"]})
    return render(request, 'diet.html')

def createFavorite(request):
    newId = Favorites(fdcId = request.POST["fdcId"])
    newId.save()
    return redirect('Diet')

def openFavorites(request):
    return render(request, 'favorites.html')
from django.http import HttpResponse
from django.shortcuts import render
import requests

def diet(request):
    url = "https://food-nutrition-information.p.rapidapi.com/foods/search"
    
    querystring = {"query":"cheese","pageSize":"1","pageNumber":"1"}

    headers = {
        'x-rapidapi-host': "food-nutrition-information.p.rapidapi.com",
        'x-rapidapi-key': "5dc8a618c5msh4ef8167e50b8d14p183fa9jsn573f8dbba635"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return render(request, 'diet.htm', {'response': response})
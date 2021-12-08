from django.urls import path

from . import views

urlpatterns = [
    path('', views.Diet, name='Diet'),
    path('favorites', views.createFavorite),
    path('listFavorits', views.openFavorites),
    path('backHome', views.Diet, name='Diet')
]

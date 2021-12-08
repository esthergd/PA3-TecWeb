from django.db import models


class Dieta(models.Model):
    title = models.CharField(max_length=200)

class Favorites(models.Model):
    fdcId = models.CharField(max_length=200)

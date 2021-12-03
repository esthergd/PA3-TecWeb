from django.db import models


class Dieta(models.Model):
    title = models.CharField(max_length=200)

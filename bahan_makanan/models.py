from django.db import models

class FoodMaterial(models.Model):
    name = models.CharField(max_length=50)
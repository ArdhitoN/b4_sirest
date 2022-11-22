from django.db import models

class FoodCategory(models.Model):
    name = models.CharField(max_length=50)
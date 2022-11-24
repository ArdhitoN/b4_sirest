from django.db import models

class RestaurantCategory(models.Model):
    name = models.CharField(max_length=50)
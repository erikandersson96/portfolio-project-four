from django.db import models
from recipes.models import Recipe
from django.contrib.auth.models import User


class Favorite(models.Model):
    """
    Model for favorite recipe
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.user},favorite )'

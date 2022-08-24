from django.contrib import admin
from .models import Favorite


@admin.register(Favorite)
class FavoritesAdmin(admin.ModelAdmin):
    """
    Admin for favorite recipes
    """
    list_display = ('user', 'favorite_recipe')

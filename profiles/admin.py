from django.contrib import admin
from .models import Favorite


class FavoritesAdmin(admin.ModelAdmin):
    """
    Admin for favorite recipes
    """
    list_display = ('user', 'favorite_recipe')


# Register the models
admin.site.register(Favorite, FavoritesAdmin)

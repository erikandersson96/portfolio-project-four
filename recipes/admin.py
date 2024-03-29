from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin use summernote for recipe
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    summernote_fields = ('method', 'ingredients')


# Register the models
admin.site.register(Recipe, RecipeAdmin)

from django.shortcuts import render
from django.views import generic
from .models import Recipe


class RecipeListView(generic.ListView):
    """
    Defines how the recipes are listed on the
    home page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'base.html'
    paginate_by = 6

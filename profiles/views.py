from django.shortcuts import render, get_object_or_404, redirect
from .models import Favorite
from recipes.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def add_favorite(request, slug):
    """
    Add favorite recipe to list
    """
    # item = get_object_or_404(Recipe, slug=slug)
    # Favorite.objects.create(user=request.user, slug=slug)
    # return redirect(reverse('recipe_detail', args=[slug]))

    current_user = request.user
    current_recipe = get_object_or_404(Recipe, slug=slug)
    Favorite.objects.create(user=current_user, favorite_recipe=current_recipe)
    return redirect(reverse('recipe_detail', args=[slug]))

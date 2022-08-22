from django.shortcuts import render, get_object_or_404, redirect
from .models import Favorite
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def add_favorite(request, slug):
    """
    Add favorite recipe to list
    """
    item = get_object_or_404(request, slug=slug)
    Favorite.objects.create(user=User, slug=slug)
    return redirect(reverse('recipe_detail', args=[slug]))

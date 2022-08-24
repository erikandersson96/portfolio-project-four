from django.shortcuts import render, get_object_or_404, redirect
from .models import Favorite
from recipes.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View, generic
from django.core.exceptions import PermissionDenied


class ProfileFavorite(generic.ListView):
    model = Recipe
    template_name = 'user_favorite.html'

    def get_queryset(self, *args, **kwargs):
        queryset = Favorite.objects.filter(user=self.request.user)
        return queryset


@login_required
def remove_favorite(slug):
    """
    Remove from favorite recipe list
    """
    remove_user_favorite = Favorite.objects.get(slug=slug)
    if remove_user_favorite.user == request.user:
        remove_user_favorite.delete()
    else:
        raise PermissionDenied()
    return redirect('profile_favorite')


@login_required
def add_favorite(request, slug):
    """
    Add favorite recipe to list
    """
    current_user = request.user
    current_recipe = get_object_or_404(Recipe, slug=slug)
    Favorite.objects.create(user=current_user, favorite_recipe=current_recipe)
    return redirect(reverse('recipe_detail', args=[slug]))

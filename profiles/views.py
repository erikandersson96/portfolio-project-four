from django.shortcuts import render, get_object_or_404, redirect
from .models import Favorite
from recipes.models import Recipe
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import View, generic
from django.core.paginator import EmptyPage, Paginator


class SafePaginator(Paginator):
    """
    Prevent user from manually type wrong page
    in the adressbar other then those existing
    """
    def validate_number(self, number):
        try:
            return super(SafePaginator, self).validate_number(number)
        except EmptyPage:
            if number > 1:
                return self.num_pages
            else:
                raise


class ProfileFavorite(generic.ListView):
    model = Recipe
    template_name = 'user_favorite.html'
    paginator_class = SafePaginator
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        queryset = Favorite.objects.filter(user=self.request.user)
        return queryset


@login_required
def remove_favorite(request, slug):
    """
    Remove from favorite recipe list
    """
    current_user = request.user
    current_recipe = get_object_or_404(Recipe, slug=slug)
    Favorite.objects.get(
        user=current_user, favorite_recipe=current_recipe).delete()
    return redirect('profile_favorite')


@login_required
def add_favorite(request, slug):
    """
    Add favorite recipe to list
    """
    current_user = request.user
    current_recipe = get_object_or_404(Recipe, slug=slug)
    Favorite.objects.get_or_create(
        user=current_user, favorite_recipe=current_recipe)
    return redirect(reverse('recipe_detail', args=[slug]))

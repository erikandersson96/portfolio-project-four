from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from .forms import RecipeForm


class RecipeListView(generic.ListView):
    """
    Defines how the recipes are listed on the
    home page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    Class for a single recipe view
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Creates the view for a single specific recipe
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "recipe_form": RecipeForm(),
            },
        )

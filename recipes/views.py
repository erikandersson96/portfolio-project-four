from django.shortcuts import render, get_object_or_404, redirect
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
            },
        )


def edit_recipe(request, slug):
    """
    View for edit recipe
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)
    context = {
        "recipe_form": recipe_form,
        "recipe": recipe
    }
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm(instance=recipe)
    return render(request, "edit_recipe.html", context)


def delete_recipe(request, slug):
    """
    View for delete recipe
    """
    recipe = Recipe.objects.get(slug=slug)
    recipe.delete()
    return redirect('home')

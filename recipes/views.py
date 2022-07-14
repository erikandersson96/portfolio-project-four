from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
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

# class edit_recipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     """
#     View for edit recipe
#     """
#     model = Recipe
#     template_name = 'edit_recipe.html'
#     form_class = RecipeForm

#     def test_func(self):
#         return Recipe.objects.author == self.request.user

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


def add_recipe(request):
    """
    View for add recipe
    """
    recipe_form = RecipeForm(request.POST or None, request.FILES or None)
    context = {
        'recipe_form': recipe_form,
    }

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        print("hello123")
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.author = request.user
            recipe_form.status = 1
            recipe_form.save()
            return redirect('home')
    else:
        recipe_form = RecipeForm()
    return render(request, "add_recipe.html", context)


# def delete_recipe(request, slug):
#     """
#     View for delete recipe
#     """
#     recipe = Recipe.objects.get(slug=slug)
#     recipe.delete()
#     return redirect('home')

class delete_recipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for delete recipe
    """
    model = Recipe
    success_url = reverse_lazy('home')

    def test_func(self):
        return Recipe.objects.author == self.request.user

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Recipe
from .forms import RecipeForm
from django.core.paginator import EmptyPage, Paginator
from django.contrib import messages


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


class RecipeListView(generic.ListView):
    """
    Defines how the recipes are listed on the
    home page
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginator_class = SafePaginator
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


@login_required
def edit_recipe(request, slug):
    """
    View for edit recipe
    """
    recipe = get_object_or_404(Recipe, slug=slug)
    if recipe.author == request.user:
        recipe_form = RecipeForm(request.POST or None, instance=recipe)
        context = {
            "recipe_form": recipe_form,
            "recipe": recipe
        }
        if request.method == "POST":
            recipe_form = RecipeForm(
                request.POST, request.FILES, instance=recipe)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                messages.success(request, (
                    "Recipe has been edited successfully."))
                return redirect('home')
        else:
            recipe_form = RecipeForm(instance=recipe)
        return render(request, "edit_recipe.html", context)
    else:
        raise PermissionDenied()
    return redirect('home')


@login_required
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
            messages.success(request, (
                    "Recipe has been added successfully."))
            return redirect('home')
    else:
        recipe_form = RecipeForm()
    return render(request, "add_recipe.html", context)


@login_required
def delete_recipe(request, slug):
    """
    View for delete recipe
    """
    recipe = Recipe.objects.get(slug=slug)
    if recipe.author == request.user:
        recipe.delete()
    else:
        raise PermissionDenied()
    return redirect('home')

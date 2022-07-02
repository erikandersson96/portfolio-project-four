from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('edit-recipe/<slug:slug>', views.edit_recipe, name='edit_recipe'),
    path('delete-recipe/<slug:slug>', views.delete_recipe, name='delete_recipe'),
]

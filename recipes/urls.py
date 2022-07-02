from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]

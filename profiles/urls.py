from . import views
from django.urls import path


urlpatterns = [
    path('add_favorite/<slug:slug>/', views.add_favorite, name='add_favorite'),
]

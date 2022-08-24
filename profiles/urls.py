from . import views
from django.urls import path


urlpatterns = [
    path(
        '', views.ProfileFavorite.as_view(),
        name='profile_favorite'),
    path('add_favorite/<slug:slug>', views.add_favorite, name='add_favorite'),
]

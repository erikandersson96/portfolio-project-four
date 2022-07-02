from django import forms
from .models import Recipe
from django_summernote.widgets import SummernoteInplaceWidget


class RecipeForm(forms.ModelForm):
    """
    Form for adding a recipe
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'excerpt',
            'difficulty',
            'serves',
            'prep_time',
            'cook_time',
            'ingredients',
            'instructions',
            'meal_image',
        ]

        widgets = {
            'ingredients': SummernoteInplaceWidget(),
            'instructions': SummernoteInplaceWidget()
        }
    
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY = ((0, "Easy"), (1, "Medium"), (2, "Advanced"))
MEASUREMENT = ((0, "kg"), (1, "grams"), (2, "liter"), (3, "deciliter"), (
    4, "tbsp"), (5, "tsp"), (6, "ounce"), (7, "cup"))

class Recipe(models.Model):
    """
    Recipe model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True,)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes")
    excerpt = models.TextField(
        blank=True, help_text="Write a short description of the recipe")
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    prep_time = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    difficulty = models.IntegerField(choices=DIFFICULTY, default=0)
    serves = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(14),
            MinValueValidator(1)
        ])
    cook_time = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(300),
            MinValueValidator(1)
        ])
    ingredients = models.TextField()
    measurement = models.IntegerField(choices=MEASUREMENT, default=1)
    instructions = models.TextField()
    meal_image = CloudinaryField('image', default='placeholder')

    class Meta:
        """
        Group the recipes from first created to last
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string for the title
        """
        return str(self.title)

    def author_edit(self, request, slug):
        """
        Allows the author of the recipe to edit it
        """
        if self.author:
            return True
        else:
            return False
        
    def author_delete(self, request, slug):
        """
        Allows the author of the recipe to delete it
        """
        if self.author:
            return True
        else:
            return False

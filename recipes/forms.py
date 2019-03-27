from django import forms
from .models import Recipes, Ingredients


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'instruction']
        localized_fields = (Ingredients.objects.values('name'),)

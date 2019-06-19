from django_filters import rest_framework as filters
from recipes.models import Recipe

class RecipeFilter(filters.FilterSet):
    class Meta:
        model = Recipe
        fields = {
            'name': ['exact', 'icontains', 'contains']
        }
from rest_framework import serializers
from recipes import models


class ChefSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Chef
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'
        
class IngredientSerializer(serializers.ModelSerializer):
    
    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['categorie'] = instance.categorie.name
        res['categorie_id'] = instance.categorie.id
        return res

    class Meta:
        model = models.Ingredient
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recipe
        fields = '__all__'
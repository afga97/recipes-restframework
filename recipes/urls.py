
from django.conf.urls import url, include
from rest_framework import routers
from recipes.views import chef

router = routers.DefaultRouter()

router.register(r'chefs', chef.ChefViewSet)
router.register(r'ingredients', chef.IngredientViewSet)
router.register(r'categories', chef.CategorieViewSet)
router.register(r'recipes', chef.RecipeViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]

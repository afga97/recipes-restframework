from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from recipes import models
from recipes.filters import filters as FilterRecipes
from recipes import serializers


class BaseViewSet(viewsets.ModelViewSet):    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if not request.GET.get('nopaginate'):
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChefViewSet(BaseViewSet):
    """
    API para crear, listar, actualizar y eliminar un chef
    """
    queryset = models.Chef.objects.all()
    serializer_class = serializers.ChefSerializer
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter, )
    ordering_fields = '__all__'
    
class IngredientViewSet(BaseViewSet):
    """
    API para crear, listar, actualizar y eliminar un ingrediente
    """
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = '__all__'
    search_fields = ('name', )


class CategorieViewSet(BaseViewSet):

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorieSerializer
    filter_backends = (DjangoFilterBackend,filters.OrderingFilter,)
    ordering_fields = '__all__'

class RecipeViewSet(BaseViewSet):

    queryset = models.Recipe.objects.prefetch_related('ingredients').all()
    serializer_class = serializers.RecipeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filterset_class = FilterRecipes.RecipeFilter
    ordering_fields = ('id', 'name')
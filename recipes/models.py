
from django.db import models
from recipes.functions import get_recipe_image_folder
# Create your models here.
class Chef(models.Model):

    name = models.CharField('Nombre', max_length=40)
    surname = models.CharField('Apellido', max_length=40)
    edad = models.CharField('Edad', max_length=5)

    class Meta:
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"

    def __str__(self):
        return "{}".format(self.name)

class Recipe(models.Model):

    name = models.CharField('Nombre', max_length=40)
    description = models.TextField('Descripción', null=True, blank=True, max_length=650)
    image = models.FileField('Imagen', upload_to=get_recipe_image_folder)
    ingredients = models.ManyToManyField('Ingredient', verbose_name="ingredients", related_name="ingredients")

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
    
    def __str__(self):
        return "{} {}".format(self.pk, self.name)

class Ingredient(models.Model):

    name = models.CharField('Nombre', max_length=40)
    description = models.TextField('Descripción')
    categorie = models.ForeignKey('Category', related_name='categorie')
    
    class Meta:
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)

class Category(models.Model):

    name = models.CharField('Nombre', max_length=40)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)

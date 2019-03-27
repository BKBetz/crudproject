from django.db import models

# Create your models here.


class Ingredients(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.ingredient

    class Meta:
        verbose_name_plural = 'Ingredients'
    pass


class Recipes(models.Model):
    title = models.CharField(max_length=50)
    instruction = models.TextField()
    ingredients = models.ManyToManyField(Ingredients, related_name="recipes")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Recipes'


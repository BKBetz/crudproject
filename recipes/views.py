from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipes
from .forms import RecipeForm
# Create your views here.


def index(request):

    recipes = Recipes.objects.all()

    context = {
        'recipes': recipes
    }

    return HttpResponse(render(request, 'recipes/index.html', context))


def details(request, id):

    recipe = Recipes.objects.get(id=id)

    context = {
        'recipe': recipe
    }

    return HttpResponse(render(request, 'recipes/details.html', context))


def add(request):

    form = RecipeForm(request.POST)

    return HttpResponse(render(request, 'recipes/add.html', {'form': form}))


def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            form.save()

            recipes = Recipes.objects.all()

            context = {
                'recipes': recipes
            }

            return HttpResponse(render(request, 'recipes/index.html', context))

    else:
        return HttpResponse('error')


def edit(request, id):
    recipe = Recipes.objects.get(id=id)

    context = {
        'recipe': recipe
    }

    return HttpResponse(render(request, 'recipes/edit.html', context))


def delete(request, id):

    recipe = Recipes.objects.get(id=id)

    context = {
        'recipe': recipe
    }

    return HttpResponse(render(request, 'recipes/delete.html', context))

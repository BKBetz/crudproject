from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.


def index(request):

    users = User.objects.all()

    context = {
        'users': users
    }
    return render(request, 'users/index.html', context)


def details(request, id):

    user = User.objects.get(id=id)

    context = {
        'user': user
    }

    return render(request, 'users/details.html', context)

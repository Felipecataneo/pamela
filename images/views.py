from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    categories = Paciente.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'imagesmain/index.html', context)

@login_required
def categoryPage(request, slug):

    category = Paciente.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'imagesmain/category.html', context)


def imageDetailPage(request, slug1, slug2):

    category = Paciente.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)

    context = {}
    context['category'] = category
    context['image'] = image

    return render(request, 'imagesmain/image.html', context)

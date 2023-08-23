from django.shortcuts import render ,redirect
from . models import Ciods , Publication

def ciods(request):

    director = Ciods.objects.filter(level = 1)
    professors = Ciods.objects.filter(level = 2)
    employees = Ciods.objects.filter(level = 3)
    pub_count = Publication.objects.all().count()

    context = {'employees':employees, 'director':director, 'professors':professors , 'pub_count':pub_count}
    return render(request,'ciods/home.html', context)

def pulblication(request):
    pulblications = Publication.objects.all()
    context = {'pulblications': pulblications}
    return render(request,'ciods/publications.html', context)

from django.shortcuts import render
from .models import people
from .models import products

# Create your views here.
def home(request):
    context = {}
    return render(request, 'webpage/home.html', context)
def contactus(request):
    context = {}
    return render(request, 'webpage/contactus.html', context) 

def peoplelist(request):
    context = {}
    context['peoples'] = people.objects.all()
    return render(request, 'webpage/people.html', context) 

def productslist(request):
    context = {}
    context['productss'] = products.objects.all()
    return render(request, 'webpage/products.html', context)
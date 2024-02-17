from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from .forms import RegistrationForm

def index(request):
    products=Product.objects.all().filter(is_available=True)
    # print(products)
    return render(request, 'index.html', {'products':products})


def register(request):
    form=RegistrationForm()
    context={
        'form': form,
    }
    return render(request, 'register.html',context)

def login(request):
    return render(request, 'signin.html')
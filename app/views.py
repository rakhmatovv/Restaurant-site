from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

from .forms import *
from .models import *


@login_required(login_url='/users/sign_in/')
def home(request):
    review = Review.objects.all()
    products = Products.objects.all()
    form = BookTableForm()
    return render(request, 'home.html', {
        'form':form,
        'reviews':review,
        'products':products,
    })

def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'product_detail.html', {
        'product': product,
    })


def booked(request):
    booked = BookTable.objects.all()

    timenow = datetime.date.today()
    return render(request, 'booked_tables.html', {'booked': booked, 'timenow': timenow})



from django.shortcuts import render, redirect

from FoodApp.models import Product
from FoodApp.forms import ProductForm


# Create your views here.


def index(request):
    return render(request,'index.html')


def outofstock(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.creator = request.user
            image = form.cleaned_data['image']
            product.save()
            return redirect('outofstock')

    queryset = Product.objects.filter(quantity=0, category__is_active=True)
    context = {'products': queryset, 'form': ProductForm}
    return render(request, 'outofstock.html', context=context)
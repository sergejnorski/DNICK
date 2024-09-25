from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404


# Create your views here.
def outofstock(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.kreator = request.user
            fotografija = form.cleaned_data['fotografija']
            product.save()
            return redirect('outofstock')
    queryset = Product.objects.filter(kolicina=0, kategorija__isActive=True)
    context = {'products': queryset, 'form': ProductForm}
    return render(request, "outofstock.html", context=context)


def edit_outofstock(request, product_id):
    product = get_object_or_404(Product, id=product_id, kreator=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('outofstock')
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, "edit_product.html", context=context)


def delete_outofstock(request, product_id):
    product = get_object_or_404(Product, id=product_id, kreator=request.user)
    if request.method == "POST":
        product.delete()
        return redirect('outofstock')
    context = {'product': product}
    return render(request, "delete_product.html", context=context)
